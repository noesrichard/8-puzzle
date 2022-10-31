from puzzle import Puzzle
from tree import Tree
from printer import TreePrinter
from menus import select_init_state, select_objective_state, start_menu, menu
from utils import random_puzzle


def main():

    # seleccionamos estado inicial 
    init = select_init_state()
    # seleccion estado objetivo
    objective = select_objective_state()

    # creamos estado objetivo
    puzzle = Puzzle(init, objective)

    # si el puzzle no es solucionable creamos uno nuevo
    while not puzzle.is_solvable():
        puzzle.matrix = random_puzzle()

    # menu para comenzar a resolver
    start_menu(puzzle)

    # creamos el arbol y lo resolvemos
    tree = Tree(puzzle)
    tree.solve()

    # impresora
    printer = TreePrinter(tree)

    # menu
    menu(printer)


if __name__ == "__main__":
    main()

#4 5 8 
#7 0 1 
#3 2 6

#6 1 2 
#3 8 4 
#5 0 7 
