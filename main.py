from puzzle import Puzzle
from tree import Tree
from printer import TreePrinter
from menus import select_init_state, select_objective_state, start_menu, menu
from utils import random_puzzle


def main():
    init = select_init_state()
    objective = select_objective_state()

    puzzle = Puzzle(init, objective)

    while not puzzle.is_solvable():
        puzzle.matrix = random_puzzle()

    start_menu(puzzle)

    tree = Tree(puzzle)
    tree.solve()

    printer = TreePrinter(tree)

    menu(printer)


if __name__ == "__main__":
    main()

#4 5 8 
#7 0 1 
#3 2 6

#6 1 2 
#3 8 4 
#5 0 7 
