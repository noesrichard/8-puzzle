from tree import Tree


class TreePrinter:
    def __init__(self, tree: Tree) -> None:
        self.tree = tree
        self.root = tree.root
        self.color = '\033[93m'
        self.end = '\033[0m'

    # imprime el arbol
    def print_tree(self):
        if self.root:
            self.print_node(self.root)
        else:
            print("None root")

    def print_tree_info(self):
        print(f"Numero de hojas: {len(self.tree.leafs)}")
        print(f"Numero de nodos abiertos: {self.tree.open_nodes}")

    def print_formatted_node_info(self, node, prefix):
        is_solved = node.puzzle.is_solved()
        text = ""
        if is_solved:
            text += self.color
        text += f"{prefix} g(n) = {node.g()}, h(n) = {node.puzzle.h()}, f(n) = {node.f()}, hoja={' SI' if node.is_leaf() else ' NO'} "
        if is_solved:
            text += f"{'****SOLUCION*****' if is_solved else ''}{self.end}"
        print(text)

    # imprime el nodo y sus hijos de manera recursiva
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
