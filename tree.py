from node import Node
from puzzle import Puzzle
class Tree:
    def __init__(self, puzzle: Puzzle) -> None:
        self.root = None
        self.puzzle = puzzle
        self.solutions = []

    def generate(self) -> None:
        self.root = Node(self.puzzle)
        self.current = self.root
        self.previous = self.current
        solution = None
        i = 0
        while solution is None:

            i += 1
            lowest = self.root.search_first_leaf_node()
            self.current = self.root.search_low_leaf_node_f(lowest)

            if self.current:

                response = self.current.generate()

                if response is not None:
                    self.solutions.append(response)

                    solution = response

            self.previous = self.current

    
