from node import Node
from puzzle import Puzzle
class Tree:
    def __init__(self, puzzle) -> None:
        self.root = None
        self.puzzle = puzzle
        self.solutions = []

    def generate(self) -> None:
        self.root = Node(self.puzzle)
        self.current = self.root
        self.previous = self.current
        solution = None
        while solution is None:
            self.current = self.search_lowest_leaf_node_f()
            self.print()
            if self.current == self.previous:
                self.current = self.root
            if self.current:
                response = self.current.generate()
                if response is not None:
                    self.solutions.append(response)
                    solution = response
            self.previous = self.current

    def search_lowest_leaf_node_f(self):
        if self.root:
            return self.root.search_lowest_leaf_node_f(self.current)        
        return None

    def print(self):
        if self.root:
            self.root.print()
        else:
            print("None root")
