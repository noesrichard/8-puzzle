from puzzle import Puzzle, Moves
from tree import Tree
from node import Node

UP = Moves.UP
DOWN = Moves.DOWN
RIGHT = Moves.RIGHT
LEFT = Moves.LEFT

if __name__ == "__main__":
    init = [
        [4,1,2]
        ,[5,6,8]
        ,[7,3,0]
    ]
    init2 = [
        [4,6,1],
        [5,3,2],
        [0,7,8]
    ]
    obj = [ 
        [1,2,3]
        ,[4,5,6]
        ,[7,8,0]
    ]
    p = Puzzle(init2, obj)
    tree = Tree(p)
    tree.generate()
