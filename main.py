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
    obj = [ 
        [1,2,3]
        ,[4,5,6]
        ,[7,8,0]
    ]
    p = Puzzle(init, obj)
    tree = Tree(p)
    tree.generate()
    print("----------------------------------PRINT TREE---------------------------------------")
    tree.print()
    lowest = tree.search_lowest_leaf_node_f()
    if lowest:
        print(lowest.print_alone())
        print(lowest.g)