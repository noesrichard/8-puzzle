from tree import Tree


class TreePrinter:
    def __init__(self, tree: Tree) -> None:
        self.tree = tree
        self.root = tree.root

    def print_tree(self):
        if self.root:
            self.print_node(self.root)
        else:
            print("None root")

    def print_node(self, node):
        spaces = " " * node.g() * 5
        prefix = spaces + "|__" if node.parent else ""
        print(
            f"{prefix} g(n) = {node.g()}, h(n) = {node.puzzle.h()}, f(n) = {node.f()}, hoja={' SI' if node.is_leaf() else ' NO'} {'****SOLUCION*****' if node.puzzle.is_solved() else ''}"
        )
        print(node.puzzle.print(prefix))
        if node.children:
            for child in node.children:
                self.print_node(child)

    def print_as_child(self, node):
        spaces = "  "
        prefix = spaces + "|__" if node.parent else ""
        print(
            f"{prefix} g(n) = {node.g()}, h(n) = {node.puzzle.h()}, f(n) = {node.f()}, hoja={' SI' if node.is_leaf() else ' NO'} {'****SOLUCION*****' if node.puzzle.is_solved() else ''}"
        )
        print(node.puzzle.print(prefix))
        if node.children:
            for child in node.children:
                self.print_node(child)

    def print_alone(self, node):
        print(f"f = {node.f()}")
        print(node.puzzle.print())

    def print_with_children(self, node):
        print(
            f"g(n) = {node.g()}, h(n) = {node.puzzle.h()}, f(n) = {node.f()}, hoja={' SI' if node.is_leaf() else ' NO'} {'****SOLUCION*****' if node.puzzle.is_solved() else ''}"
        )
        print(node.puzzle.print())
        if node.children:
            for child in node.children:
                self.print_as_child(child)
