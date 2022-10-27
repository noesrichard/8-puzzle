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
        while (self.solution is None 
            or self.solution is not self.root.search_leaf_node_lower_or_equal_than(self.solution)):
            i += 1
            print(f"Busqueda: {i}")

            leaf_node = self.root.search_first_leaf_node()

            if self.root.exists_leaf_node_lower_than(leaf_node):
                self.current = self.root.search_leaf_node_lower_than(leaf_node)
            else:
                self.current = self.root.search_leaf_node_lower_or_equal_than(leaf_node)

            if self.current:

                self.solution = self.current.generate_children()

        print(f"Total de iteraciones: {i} ")



