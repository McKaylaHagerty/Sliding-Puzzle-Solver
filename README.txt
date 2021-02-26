Homework 1 - 24 Piece Problem Solver
Abigail Smith
McKayla Hagerty
2/23/2021

How To Run
----------
Make sure python is installed. On command line, navigate to the directory with puzzle.py. Type "python puzzle.py" to run. There will be a prompt for depth first or breadth first search. Press 1 for depth first and 2 for breadth first. Ctrl + C can be used to stop the program, since it will run until a solution is found.

The Problem
-----------
The goal is to use two uninformed search methods, breadth-first search and depth-first search, to solve a 24-piece sliding puzzle given certain start positions. The blank tile which is denoted with a zero throughout the problem is repeatedly switched with a neighboring tile until the order is restored (1,2,…,24,0).

The Algorithms
--------------
For both breath-first search and depth-first search, the original tile placement is provided as the start. A start value is given in the problem: “start = [[6, 18, 12, 0, 24], [13, 7, 9, 2, 17], [1, 23, 8, 14, 11], [19, 22, 3, 15, 16], [21, 5, 4, 10, 20]].” Moves are determined with the findMoves function and are dependent on matrix size and the position of the black or zero tile. Each new matrix is printed before it is searched and is checked to ensure is has not already been explored, preventing loops in the search algorithm.

Breadth-First Search
--------------------
For breadth-first search, we used a fifo list to store new moves. For each branch, its children are added to the end of the list. The branch is then removed from the front of the list, and the new front is made the current branch. For each move, the matrix, current time, and number of moves are displayed.



Depth-First Search
------------------
For depth-first search, we used a filo list to store new moves. For each branch, its children are added to the end of the list. The last move in the list is made the current branch. For each move, the matrix, current time, and number of moves are displayed.



Results for 8 Piece Puzzle
--------------------------
start=[[0,1,3], [4,2,5], [7,8,6]]

We tested the code with an 8-piece puzzle found both algorithms were successful. The execution time for breadth-first search was 0.0573 with 67 states visited. The depth-first search took slightly less time at 0.0572 while also visiting 67 states.


Results for 24 Piece Puzzle
---------------------------
start = [[6, 18, 12, 0, 24], [13, 7, 9, 2, 17], [1, 23, 8, 14, 11], [19, 22, 3, 15, 16], [21, 5, 4, 10, 20]]

When we changed our code to the 24 piece puzzle, it no longer found a solution for neither depth first or breadth first search. We ran both for an hour and found that depth first search was able to make 44,107 moves and breadth first search was able to make 43,693 moves. The longest we have run our code is overnight, with no solution for both algorithms.



Our Code Output- 8 puzzle
-------------------------

Breadth-First Search:

current state:
0 1 3
4 2 5
7 8 6
current state:
0 1 3
4 2 5
7 8 6
current state:
1 0 3
4 2 5
7 8 6
current state:
4 1 3
0 2 5
7 8 6
current state:
1 0 3
4 2 5
7 8 6
current state:
4 1 3
0 2 5
7 8 6
current state:
1 3 0
4 2 5
7 8 6
current state:
1 2 3
4 0 5
7 8 6
current state:
4 1 3
2 0 5
7 8 6
current state:
4 1 3
7 2 5
0 8 6
current state:
1 3 0
4 2 5
7 8 6
current state:
1 2 3
4 0 5
7 8 6
current state:
4 1 3
2 0 5
7 8 6
current state:
4 1 3
7 2 5
0 8 6
current state:
1 3 5
4 2 0
7 8 6
current state:
1 2 3
0 4 5
7 8 6
current state:
1 2 3
4 5 0
7 8 6
current state:
1 2 3
4 8 5
7 0 6
current state:
4 1 3
2 5 0
7 8 6
current state:
4 0 3
2 1 5
7 8 6
current state:
4 1 3
2 8 5
7 0 6
current state:
4 1 3
7 2 5
8 0 6
current state:
1 3 5
4 2 0
7 8 6
current state:
1 2 3
0 4 5
7 8 6
current state:
1 2 3
4 5 0
7 8 6
current state:
1 2 3
4 8 5
7 0 6
current state:
4 1 3
2 5 0
7 8 6
current state:
4 0 3
2 1 5
7 8 6
current state:
4 1 3
2 8 5
7 0 6
current state:
4 1 3
7 2 5
8 0 6
current state:
1 3 5
4 0 2
7 8 6
current state:
1 3 5
4 2 6
7 8 0
current state:
0 2 3
1 4 5
7 8 6
current state:
1 2 3
7 4 5
0 8 6
current state:
1 2 0
4 5 3
7 8 6
BFS:
current state:
1 2 3
4 5 6
7 8 0

solved
Execution time: 0.057343400000000155
Number of states visited: 67



Depth-First Search:

current state:
0 1 3
4 2 5
7 8 6
current state:
0 1 3
4 2 5
7 8 6
current state:
1 0 3
4 2 5
7 8 6
current state:
4 1 3
0 2 5
7 8 6
current state:
1 0 3
4 2 5
7 8 6
current state:
4 1 3
0 2 5
7 8 6
current state:
1 3 0
4 2 5
7 8 6
current state:
1 2 3
4 0 5
7 8 6
current state:
4 1 3
2 0 5
7 8 6
current state:
4 1 3
7 2 5
0 8 6
current state:
1 3 0
4 2 5
7 8 6
current state:
1 2 3
4 0 5
7 8 6
current state:
4 1 3
2 0 5
7 8 6
current state:
4 1 3
7 2 5
0 8 6
current state:
1 3 5
4 2 0
7 8 6
current state:
1 2 3
0 4 5
7 8 6
current state:
1 2 3
4 5 0
7 8 6
current state:
1 2 3
4 8 5
7 0 6
current state:
4 1 3
2 5 0
7 8 6
current state:
4 0 3
2 1 5
7 8 6
current state:
4 1 3
2 8 5
7 0 6
current state:
4 1 3
7 2 5
8 0 6
current state:
1 3 5
4 2 0
7 8 6
current state:
1 2 3
0 4 5
7 8 6
current state:
1 2 3
4 5 0
7 8 6
current state:
1 2 3
4 8 5
7 0 6
current state: 4 1 3
2 5 0
7 8 6
current state:
4 0 3
2 1 5
7 8 6
current state:
4 1 3
2 8 5
7 0 6
current state:
4 1 3
7 2 5
8 0 6
current state:
1 3 5
4 0 2
7 8 6
current state:
1 3 5
4 2 6
7 8 0
current state:
0 2 3
1 4 5
7 8 6
current state:
1 2 3
7 4 5
0 8 6
current state:
1 2 0
4 5 3
7 8 6
DFS:
current state:
1 2 3
4 5 6
7 8 0

solved
Execution time: 0.05716480000000024
Number of states visited: 67





Our Code Output- 24 puzzle
--------------------------

Breadth-First Search:

current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  2
current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  3
current state:
6   18   0   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  4
current state:
6   18   12   24   0
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  5
current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  6
current state:
6   18   0   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  7
current state:
6   18   12   24   0
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  8
current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  9
current state:
6   0   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  10
current state:
6   18   9   12   24
13   7   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  11
current state:
6   18   12   24   17
13   7   9   2   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  12
current state:
6   18   12   2   24
13   7   0   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  13
current state:
6   18   12   2   24
13   7   9   17   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  14
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  15
current state:
6   0   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  16
current state:
6   18   9   12   24
13   7   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  17
current state:
6   18   12   24   17
13   7   9   2   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  18
current state:
6   18   12   2   24
13   7   0   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  19
current state:
6   18   12   2   24
13   7   9   17   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.015625
moves:  20
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20




Depth-First Search:

current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  2
current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  3
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20

time:  0.0
moves:  4
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   0   16
21   5   4   10   20

time:  0.0
moves:  5
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   10   16
21   5   4   0   20

time:  0.0
moves:  6
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   10   16
21   5   4   20   0

time:  0.0
moves:  7
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   10   0
21   5   4   20   16

time:  0.0
moves:  8
current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   0
19   22   3   10   11
21   5   4   20   16

time:  0.0
moves:  9
current state:
6   18   12   2   24
13   7   9   14   0
1   23   8   15   17
19   22   3   10   11
21   5   4   20   16

time:  0.0
moves:  10
current state:
6   18   12   2   0
13   7   9   14   24
1   23   8   15   17
19   22   3   10   11
21   5   4   20   16

time:  0.0
moves:  11
current state:
6   18   12   0   2
13   7   9   14   24
1   23   8   15   17
19   22   3   10   11
21   5   4   20   16

time:  0.0
moves:  12
current state:
6   18   12   14   2
13   7   9   0   24
1   23   8   15   17
19   22   3   10   11
21   5   4   20   16

time:  0.0
moves:  13
current state:
6   18   12   14   2
13   7   9   15   24
1   23   8   0   17
19   22   3   10   11
21   5   4   20   16

time:  0.0
moves:  14
current state:
6   18   12   14   2
13   7   9   15   24
1   23   8   10   17
19   22   3   0   11
21   5   4   20   16

time:  0.0
moves:  15
current state:
6   18   12   14   2
13   7   9   15   24
1   23   8   10   17
19   22   3   20   11
21   5   4   0   16

time:  0.0
moves:  16
current state:
6   18   12   14   2
13   7   9   15   24
1   23   8   10   17
19   22   3   20   11
21   5   4   16   0

time:  0.0
moves:  17
current state:
6   18   12   14   2
13   7   9   15   24
1   23   8   10   17
19   22   3   20   0
21   5   4   16   11

time:  0.0
moves:  18
current state:
6   18   12   14   2
13   7   9   15   24
1   23   8   10   0
19   22   3   20   17
21   5   4   16   11

time:  0.0
moves:  19
current state:
6   18   12   14   2
13   7   9   15   0
1   23   8   10   24
19   22   3   20   17
21   5   4   16   11

time:  0.0
moves:  20
current state:
6   18   12   14   0
13   7   9   15   2
1   23   8   10   24
19   22   3   20   17
21   5   4   16   11