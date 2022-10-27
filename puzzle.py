from enum import Enum
class Moves(Enum):
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    UP = "UP"
    DOWN = "DOWN"

class Puzzle: 

    def __init__(self, matrix: list[list[int]], obj: list[list[int]]) -> None:
        self.matrix = matrix
        self.obj = obj
        self.__set_zero_position()

    def __get_position(self, number, where):
        for i in range(len(where)):
            for j in range(len(where)):
                if where[i][j] == number:
                    return [i,j]
        return [-1,-1]

    def h(self):
        total = 0
        for i in range(1,9):
            i_o, j_o = self.__get_position(i, self.matrix)
            i_f, j_f = self.__get_position(i, self.obj)
            i_h = abs(i_o-i_f)
            j_h = abs(j_o-j_f)
            total += i_h + j_h
        return total

    def __set_zero_position(self) -> None: 
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    self.i = i
                    self.j = j
    def move(self, direction: Moves) -> bool: 
        moves = {
            Moves.UP: self.__move_up,
            Moves.DOWN: self.__move_down,
            Moves.RIGHT: self.__move_right,
            Moves.LEFT: self.__move_left,
        }
        if self.check_move(direction):
            moves[direction]() 
            self.__set_zero_position()
            return True
        else:
            #print(f"Cannot move that direction: {direction} i: {self.i} j: {self.j}")
            return False

    def check_move(self, direction: Moves) -> bool: 
        directions = { 
            Moves.UP: self.i != 0,
            Moves.DOWN: self.i != 2,
            Moves.RIGHT: self.j != 2,
            Moves.LEFT: self.j != 0
        }
        return directions[direction]

    def is_solved(self) -> bool:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != self.obj[i][j]:
                    return False
        return True

    def equals(self, puzzle) -> bool:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != puzzle.matrix[i][j]:
                    return False
        return True


    def print(self, spaces = ''): 
        text = spaces + "_____ \n"
        blanks = ""
        for i in range(len(spaces)):
            if i == len(spaces)-3:
                blanks += "|"
            else:
                blanks += " "
        for row in self.matrix:
            text += blanks
            for n in row:
                text +=  str(n) + ' '
            text += '\n'
        text += spaces + '_____ '
        return text

    def print_objective(self, spaces = ''):
        text = spaces + "_____ \n"
        blanks = ""
        for i in range(len(spaces)):
            if i == len(spaces)-3:
                blanks += "|"
            else:
                blanks += " "
        for row in self.obj:
            text += blanks
            for n in row:
                text +=  str(n) + ' '
            text += '\n'
        text += spaces + '_____ '
        return text

    
    def get_matrix(self) -> list[list[int]]:
        new_matrix = []
        for row in self.matrix:
            new_row = []
            for j in row:
                new_row.append(j)
            new_matrix.append(new_row)
        return new_matrix

    def get_inv_count(self, arr):
        inv_count = 0
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count
 
    def is_solvable(self):
        inv_count = self.get_inv_count([j for sub in self.matrix for j in sub])
        return (inv_count % 2 == 0)

    def __move_up(self) -> None: 
        self.matrix[self.i][self.j] = self.matrix[self.i-1][self.j]
        self.matrix[self.i-1][self.j] = 0

    def __move_down(self) -> None: 
        self.matrix[self.i][self.j] = self.matrix[self.i+1][self.j]
        self.matrix[self.i+1][self.j] = 0

    def __move_right(self) -> None: 
        self.matrix[self.i][self.j] = self.matrix[self.i][self.j+1]
        self.matrix[self.i][self.j+1] = 0

    def __move_left(self) -> None: 
        self.matrix[self.i][self.j] = self.matrix[self.i][self.j-1]
        self.matrix[self.i][self.j-1] = 0




