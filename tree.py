from node import Node
from puzzle import Puzzle
class Tree:
    def __init__(self, puzzle: Puzzle) -> None:
        self.root = None
        self.puzzle = puzzle
        self.solution = None


    def solve(self) -> None:
        self.root = Node(self.puzzle)
        self.current = self.root
        i = 0
        while self.solution is None or self.solution is not self.root.search_leaf_node_lower_than(self.solution):
            i += 1
            print(f"Busqueda: {i}")

            lowest = self.root.search_first_leaf_node()
            self.current = self.root.search_leaf_node_lower_than(lowest)

            if self.current:

                response = self.current.generate_children()

                if response is not None:

                    self.solution = response
        print(f"Total de iteraciones: {i} ")



