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


    def solve(self) -> None:
        self.root = Node(self.puzzle)
        self.current = self.root
        self.leafs.append(self.root)
        while (self.solution is None 
            or self.solution is not self.root.search_leaf_node_lower_or_equal_than(self.solution)):
            self.iter += 1
            print(f"Busqueda: {self.iter}")

            leaf_node = self.leafs[0]
            self.current = self.root.search_leaf_node_lower_or_equal_than(leaf_node)

            if self.current:
                self.solution = self.current.generate_children()
                if self.current.children:
                    self.leafs.remove(self.current)
                    self.open_nodes += 1
                    for child in self.current.children:
                        self.leafs.append(child)

            self.leafs.sort(key=lambda hoja: hoja.f())




