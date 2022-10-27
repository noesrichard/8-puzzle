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

    def print_formatted_node_info(self, node, prefix):
        print(f"{prefix} g(n) = {node.g()}, h(n) = {node.puzzle.h()}, f(n) = {node.f()}, hoja={' SI' if node.is_leaf() else ' NO'} {'****SOLUCION*****' if node.puzzle.is_solved() else ''}")

    def print_node(self, node):
        spaces = " " * node.g() * 5
        prefix = spaces + "|__" if node.parent else ""
        self.print_formatted_node_info(node, prefix)
        print(node.puzzle.print(prefix))
        if node.children:
            for child in node.children:
                self.print_node(child)

    def print_as_child(self, node):
        spaces = "  "
        prefix = spaces + "|__" if node.parent else ""
        self.print_formatted_node_info(node, prefix)
        print(node.puzzle.print(prefix))
        if node.children:
            for child in node.children:
                self.print_node(child)

    def print_alone(self, node):
        print(f"f = {node.f()}")
        print(node.puzzle.print())

    def print_with_children(self, node):
        print(node.puzzle.print())
        self.print_formatted_node_info(node, '')
        if node.children:
            for child in node.children:
                self.print_as_child(child)

    def print_steps_solution(self):
        current = self.tree.solution
        steps = []
        while current: 
            steps.append(current.puzzle)
            current = current.parent
        steps.reverse()
        i = 0
        for puzzle in steps:
            print(f"Paso: {i}")
            print(puzzle.print())
            i += 1
