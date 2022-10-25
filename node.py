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
        print("***************NEW ITERATION***************")
        if self.parent:
            print("&&&&&&&&PARENT^^^^^^^^^")
            print(self.parent.puzzle.print())

        print("&&&&&&&&SELF^^^^^^^^^")
        print(self.puzzle.print())
        if self.puzzle.is_obj():
            return self
        for i in Moves:
            print(i)
            matrix = self.puzzle.get_matrix()
            new_puzzle = Puzzle(matrix, self.puzzle.obj)
            if new_puzzle.move(i):
                if self.parent:
                    if not self.parent.puzzle.equals(new_puzzle):
                        self.add_child(new_puzzle)
                    else: 
                        print(f"Cannot make that same move: {i}, {self.puzzle.i}, {self.puzzle.j}")
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
        if self.is_leaf():
            if lowest.f >= self.f:
                return self
        if self.children: 
            for child in self.children:
                lowest = child.search_lowest_leaf_node_f(lowest)
        return lowest

    def print(self):
        spaces = ' ' * self.g() * 4
        print(f"{spaces}f(n) = {self.f}, g(n) = {self.g()}, h(n) = {self.puzzle.h()}")
        print(self.puzzle.print(spaces))
        if self.children:
            for child in self.children:
                child.print()
    def print_alone(self):
        print(f"f = {self.f}")
        print(self.puzzle.print())
