# 8 Puzzle Solver with A* Algorithm

This project is a command-line interface (CLI) implementation of an 8 puzzle solver using the A* algorithm. The A* algorithm is an informed search algorithm commonly used for pathfinding and optimization problems. The goal of this solver is to find the shortest sequence of moves to solve the 8 puzzle.

## Getting Started

To use this 8 puzzle solver, follow the instructions below:

1. Make sure you have Python 3 installed on your system.
2. Clone this repository to your local machine or download the source code files.
3. Open a terminal or command prompt and navigate to the project directory.
4. You can run the program by executing the following command:

   ```shell
   python main.py
   ```

## Usage

When you run the program, you will be prompted to enter the starting and goal states of the puzzle. The state of the puzzle is represented as a sequence of numbers from 0 to 8, where 0 represents the empty space. Enter the numbers row by row, separating them with spaces.

For example, to input the following puzzle:

```
1 2 3
4 5 6
0 7 8
```

You would enter: 
```
1 2 3
4 5 6
0 7 8
```

And it's the same if you want to enter a desire solution. 
If you don't want an initial state and a desire solution the program will generate random states.
After entering the starting and goal states, you should confirm the states to start the program.
## Algorithm

This 8 puzzle solver uses the A* algorithm, which is an informed search algorithm that evaluates and selects the most promising moves based on a heuristic function. The A* algorithm uses a priority queue (min-heap) to explore the possible moves and selects the move with the lowest cost.

The heuristic function used in this solver is the sum of the Manhattan distances of each tile from its goal position. The Manhattan distance is the sum of the absolute differences in the x and y coordinates of two points. By using this heuristic, the algorithm can estimate the number of moves required to reach the goal state from the current state.
