from puzzle import Puzzle, Moves


class Node:
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.parent = None
        self.children = []

    def add_child(self, puzzle):
        if self.is_repeated(puzzle):
            return
        child = Node(puzzle)
        child.parent = self
        self.children.append(child)

    # comprueba si el nodo es igual que el padre, para que no se repita
    def is_repeated(self, puzzle):
        if self.parent:
            return self.parent.puzzle.equals(puzzle)


    # genera los hijos, movimientos
    def generate_children(self):
        # comprueba si el puzzle esta resuelto
        if self.puzzle.is_solved():
            return self

        # generea los movimientos si se puede
        for i in Moves:
            matrix = self.puzzle.get_matrix()
            new_puzzle = Puzzle(matrix, self.puzzle.obj)

            # comprueba si el movimiento es valido
            if new_puzzle.move(i):
                self.add_child(new_puzzle)
        return None

    def is_leaf(self):
        if len(self.children) > 0:
            return False
        return True

    # funcion de comparacion de cada nodo
    def f(self):
        return self.g() + self.puzzle.h()

    # funcion de costo del camino
    def g(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    # buscar nodos menor o igual que el nodo actual en f(n)
    def search_leaf_node_lower_or_equal_than(self, lowest):
        # si el nodo es una hoja y si es menor o igual al nodo menor se retorna a si mismo
        if self.is_leaf() and self.lower_or_equal_f_than(lowest):
            return self
        # si tiene hijos busca en sus hijos con recursivdidad
        if self.children:
            for child in self.children:
                lowest = child.search_leaf_node_lower_or_equal_than(lowest)
        return lowest

    def search_leaf_node_lower_than(self, lowest):
        # si el nodo es una hoja y si es menor o igual al nodo menor se retorna a si mismo
        if self.is_leaf() and self.lower_f_than(lowest):
            return self
        # si tiene hijos busca en sus hijos con recursivdidad
        if self.children:
            for child in self.children:
                lowest = child.search_leaf_node_lower_than(lowest)
        return lowest


    # busca si existe un nodo mejor que otro nodo
    def exists_leaf_node_lower_than(self, node) -> bool:
        if self.is_leaf() and self.lower_f_than(node):
            return True 
        exists = False
        if self.children:
            for child in self.children:
                 exists = child.exists_leaf_node_lower_than(node)
                 if exists:
                    break
        return exists

    def search_first_leaf_node(self):
        if self.is_leaf():
            return self
        if self.children:
            for child in self.children:
                return child.search_first_leaf_node()

    # comparacion entre f(n) del nodo actual y del menor
    def lower_or_equal_f_than(self, other) -> bool:
        return self.f() <= other.f()

    def lower_f_than(self, other) -> bool:
        return self.f() < other.f()

