from node import Node
from puzzle import Puzzle
class Tree:
    def __init__(self, puzzle: Puzzle) -> None:
        self.root = None
        self.puzzle = puzzle
        self.solution = None
        self.leafs = []
        self.open_nodes = 0
        self.iter = 0


    # resolver el arbol
    def solve(self) -> None:

        # creamos la raiz
        self.root = Node(self.puzzle)
        self.current = self.root

        # nodos hoja
        self.leafs.append(self.root)

        # mientras no haya solucion o la solucion no sea la menor del arbol
        while (self.solution is None 
            or self.solution is not self.root.search_leaf_node_lower_or_equal_than(self.solution)):
            self.iter += 1
            print(f"Busqueda: {self.iter}")

            # escoje la hoja de menor valor
            leaf_node = self.leafs[0]
            # busca una hoja de menor valor
            self.current = self.root.search_leaf_node_lower_or_equal_than(leaf_node)

            if self.current:
                # genera los hijos (acciones, movimientos)
                self.solution = self.current.generate_children()
                if self.current.children:

                    #elimina el nodo abierto de las hojas
                    self.leafs.remove(self.current)
                    self.open_nodes += 1

                    # agrega los nodos hijos a los nodos hojas
                    for child in self.current.children:
                        self.leafs.append(child)

            self.leafs.sort(key=lambda hoja: hoja.f())




