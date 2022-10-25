from puzzle import Puzzle, Moves
class Node: 
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.parent = None
        self.children = []
        self.f = self.g() + self.puzzle.h()

    def add_child(self, puzzle):
        child =  Node(puzzle)
        child.parent = self
        self.children.append(child)

    def generate(self): 
        if self.puzzle.is_obj():
            return self
        for i in Moves:
            matrix = self.puzzle.get_matrix()
            new_puzzle = Puzzle(matrix, self.puzzle.obj)
            if new_puzzle.move(i):
                if self.parent:
                    if not self.parent.puzzle.equals(new_puzzle):
                        self.add_child(new_puzzle)
                    else: 
                        print(f"Cannot make that same move: {i}, position = ({self.puzzle.i}, {self.puzzle.j})")
                if not self.parent:
                    self.add_child(new_puzzle)
        return None

    def is_leaf(self): 
        if len(self.children) > 0:
            return False
        return True

    def f_value(self):
        return self.g() + self.puzzle.h()

    def g(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def search_lowest_leaf_node_f(self, lowest):
        f_lowest = lowest.g() + lowest.puzzle.h()
        f_current = self.g() + self.puzzle.h() 
        if self.is_leaf():
            if f_lowest >= f_current:
                return self
        if self.children: 
            for child in self.children:
                lowest = child.search_lowest_leaf_node_f(lowest)
        return lowest
    
    def search_high_leaf_node_f(self, highest):
        if self.is_leaf() and self.g() + self.puzzle.h() > highest.g() + highest.puzzle.h():
            return self
        if self.children: 
            for child in self.children:
                highest = child.search_high_leaf_node_f(highest)
        return highest
    
    def search_low_leaf_node_f(self, lowest):
        if self.is_leaf() and self.g() + self.puzzle.h() < lowest.g() + lowest.puzzle.h():
            return self
        if self.children: 
            for child in self.children:
                lowest = child.search_low_leaf_node_f(lowest)
        return lowest




    def print(self):
        f_current = self.g() + self.puzzle.h() 
        spaces = ' ' * self.g() * 5
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix} g(n) = {self.g()}, h(n) = {self.puzzle.h()}, f(n) = {f_current}, hoja={' SI' if self.is_leaf() else ' NO'} {'****SOLUCION*****' if self.puzzle.is_obj() else ''}")
        print(self.puzzle.print(prefix))
        if self.children:
            for child in self.children:
                child.print()

    def print_as_child(self):
        f_current = self.g() + self.puzzle.h() 
        spaces = '  '
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix} g(n) = {self.g()}, h(n) = {self.puzzle.h()}, f(n) = {f_current}, hoja={' SI' if self.is_leaf() else ' NO'} {'****SOLUCION*****' if self.puzzle.is_obj() else ''}")
        print(self.puzzle.print(prefix))
        if self.children:
            for child in self.children:
                child.print()

    def print_alone(self):
        f_current = self.g() + self.puzzle.h() 
        print(f"f = {f_current}")
        print(self.puzzle.print())

    def print_with_children(self):
        f_current = self.g() + self.puzzle.h() 
        print(f"g(n) = {self.g()}, h(n) = {self.puzzle.h()}, f(n) = {f_current}, hoja={' SI' if self.is_leaf() else ' NO'} {'****SOLUCION*****' if self.puzzle.is_obj() else ''}")
        print(self.puzzle.print())
        if self.children:
            for child in self.children:
                child.print_as_child()
