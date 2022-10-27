from utils import random_puzzle

def input_puzzle(): 
    objective = []
    list = []
    for i in range(3):
        list = input(f"Fila {i+1}:").split(" ")
        objective.append([int(n) for n in list])
    return objective

def start_menu(puzzle):
    print("Puzzle seleccionado")
    print("Estado Inicial")
    print(puzzle.print())
    print("Estado Objetivo")
    print(puzzle.print_objective())
    option = int(input("Ingrese 1 para continuar: "))
    if option != 1: 
        exit()

def menu(printer):
    stop = True
    while stop:
        options = {
            1: printer.print_tree,
            2: printer.print_steps_solution,
        }
        option = int(
            input(
                " -----MENU----- \n [1] Mostar Arbol \n [2] Mostrar pasos para la solucion \n [0] Salir \n Respuesta: "
            )
        )
        if option == 0:
            exit()
        else:
            options[option]()


def select_objective():
    options = {
        1: [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        2: [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
    }
    option = int(
        input(
            """Seleccione el estado objetivo: 
 [1] 0 1 2 
     3 4 5
     6 7 8

 [2] 1 2 3
     4 5 6 
     7 8 0

 [3] Personalizado 
 Respuesta: """
        )
    )
    if option == 3:
        print(
            """Inserte el objetivo dejando un espacio por numero, terminada una fila de un enter para ingresar la otra
Ej. Fila 1:1 2 3
    Fila 2:4 5 6
    Fila 3:7 8 0
            """
        )
        return input_puzzle()
    else:
        return options[option]


def select_init_state():
    option = int(
        input(
            """Seleccion el estado inicial:
[1] Aleatorio 
[2] Personalizado 
Respuesta: """
        )
    )
    if option == 1:
        return random_puzzle()
    else:
        print(
            """Inserte el estado inicial dejando un espacio por numero, terminada una fila de un enter para ingresar la otra. 
Ej. Fila 1:1 2 3
    Fila 2:4 5 0
    Fila 3:7 8 6
        """
        )
        return input_puzzle()


