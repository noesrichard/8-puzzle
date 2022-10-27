from puzzle import Puzzle, Moves


class Node:
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.parent = None
        self.children = []

    def add_child(self, puzzle):
        if self.is_repeated(puzzle):
            #print( f"Cannot make that same move: position = ({self.puzzle.i}, {self.puzzle.j})")
            return
        child = Node(puzzle)
        child.parent = self
        self.children.append(child)

    def is_repeated(self, puzzle):
        if self.parent:
            return self.parent.puzzle.equals(puzzle)

    def generate(self):
        if self.puzzle.is_solved():
            return self
        for i in Moves:
            matrix = self.puzzle.get_matrix()
            new_puzzle = Puzzle(matrix, self.puzzle.obj)
            #print(f"Move done: {i} init: {self.puzzle.i},{self.puzzle.j} next: {new_puzzle.i},{new_puzzle.j}")
            if new_puzzle.move(i):
                self.add_child(new_puzzle)
        return None

    def is_leaf(self):
        if len(self.children) > 0:
            return False
        return True

    def f(self):
        return self.g() + self.puzzle.h()

    def g(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def search_low_leaf_node_f(self, lowest):
        if self.is_leaf() and self.lower_or_equal_f_than(lowest):
            return self
        if self.children:
            for child in self.children:
                lowest = child.search_low_leaf_node_f(lowest)
        return lowest

    def search_first_leaf_node(self):
        if self.is_leaf():
            return self
        if self.children:
            for child in self.children:
                return child.search_first_leaf_node()

    def lower_or_equal_f_than(self, other) -> bool:
        return self.f() <= other.f()

