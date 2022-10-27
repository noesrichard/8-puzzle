from random import shuffle
def random_puzzle():
    cells = []
    numbers = list(range(0, 9))
    shuffle(numbers)
    for row in range(3):
        cells.append([])
        for col in range(3):
            cells[row].append(numbers.pop())
    return cells

def print_selection(puzzle):
    print("Puzzle seleccionado")
    print("Estado Inicial")
    print(puzzle.print())
    print("Estado Objetivo")
    print(puzzle.print_objective())

