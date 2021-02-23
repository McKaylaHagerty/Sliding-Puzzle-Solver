# Homework 1 - 24 Piece Problem Solver
Abigail Smith  
McKayla Hagerty  
2/23/2021  

## The Problem
The goal is to use two uninformed search methods, breadth-first search and depth-first search, to solve a 24-piece sliding puzzle given certain start positions. The blank tile which is denoted with a zero throughout the problem is repeatedly switched with a neighboring tile until the order is restored (1,2,…,24,0). 

## The Algorithms
For both breath-first search and depth-first search, the original tile placement is provided as the start. A start value is given in the problem: “start = [[6, 18, 12, 0, 24], [13, 7, 9, 2, 17], [1, 23, 8, 14, 11], [19, 22, 3, 15, 16], [21, 5, 4, 10, 20]].” Moves are determined with the findMoves function and are dependent on matrix size and the position of the black or zero tile. Each new matrix is printed before it is searched and is checked to ensure is has not already been explored, preventing loops in the search algorithm.  

### Breadth-First Search

### Depth-First Search 

## Results for 8 Piece Puzzle
start=[[0,1,3], [4,2,5], [7,8,6]]

We tested the code with an 8-piece puzzle found both algorithms were successful. The execution time for breadth-first search was 0.0573 with 67 states visited. The deepth-first search took signtly less time at 0.0572 while also visiting 67 states.

### Breadth-First Search

current state:
0   1   3
4   2   5
7   8   6

current state:
0   1   3
4   2   5
7   8   6

current state:
1   0   3
4   2   5
7   8   6

current state:
4   1   3
0   2   5
7   8   6

current state:
1   0   3
4   2   5
7   8   6

current state:
4   1   3
0   2   5
7   8   6

current state:
1   3   0
4   2   5
7   8   6

current state:
1   2   3
4   0   5
7   8   6

current state:
4   1   3
2   0   5
7   8   6

current state:
4   1   3
7   2   5
0   8   6

current state:
1   3   0
4   2   5
7   8   6

current state:
1   2   3
4   0   5
7   8   6

current state:
4   1   3
2   0   5
7   8   6

current state:
4   1   3
7   2   5
0   8   6

current state:
1   3   5
4   2   0
7   8   6

current state:
1   2   3
0   4   5
7   8   6

current state:
1   2   3
4   5   0
7   8   6

current state:
1   2   3
4   8   5
7   0   6

current state:
4   1   3
2   5   0
7   8   6

current state:
4   0   3
2   1   5
7   8   6

current state:
4   1   3
2   8   5
7   0   6

current state:
4   1   3
7   2   5
8   0   6

current state:
1   3   5
4   2   0
7   8   6

current state:
1   2   3
0   4   5
7   8   6

current state:
1   2   3
4   5   0
7   8   6

current state:
1   2   3
4   8   5
7   0   6

current state:
4   1   3
2   5   0
7   8   6

current state:
4   0   3
2   1   5
7   8   6

current state:
4   1   3
2   8   5
7   0   6

current state:
4   1   3
7   2   5
8   0   6

current state:
1   3   5
4   0   2
7   8   6

current state:
1   3   5
4   2   6
7   8   0

current state:
0   2   3
1   4   5
7   8   6

current state:
1   2   3
7   4   5
0   8   6

current state:
1   2   0
4   5   3
7   8   6

BFS:
current state:
1   2   3
4   5   6
7   8   0

solved  
Execution time:  0.057343400000000155  
Number of states visited:  67  

### Depth-First Search 

current state:
0   1   3
4   2   5
7   8   6

current state:
0   1   3
4   2   5
7   8   6

current state:
1   0   3
4   2   5
7   8   6

current state:
4   1   3
0   2   5
7   8   6

current state:
1   0   3
4   2   5
7   8   6

current state:
4   1   3
0   2   5
7   8   6

current state:
1   3   0
4   2   5
7   8   6

current state:
1   2   3
4   0   5
7   8   6

current state:
4   1   3
2   0   5
7   8   6

current state:
4   1   3
7   2   5
0   8   6

current state:
1   3   0
4   2   5
7   8   6

current state:
1   2   3
4   0   5
7   8   6

current state:
4   1   3
2   0   5
7   8   6

current state:
4   1   3
7   2   5
0   8   6

current state:
1   3   5
4   2   0
7   8   6

current state:
1   2   3
0   4   5
7   8   6

current state:
1   2   3
4   5   0
7   8   6

current state: 
1   2   3
4   8   5
7   0   6

current state:
4   1   3
2   5   0
7   8   6

current state:
4   0   3
2   1   5
7   8   6

current state:
4   1   3
2   8   5
7   0   6

current state:
4   1   3
7   2   5
8   0   6

current state:
1   3   5
4   2   0
7   8   6

current state:
1   2   3
0   4   5
7   8   6

current state:
1   2   3
4   5   0
7   8   6

current state:
1   2   3
4   8   5
7   0   6

current state:
4   1   3
2   5   0
7   8   6

current state:
4   0   3
2   1   5
7   8   6

current state:
4   1   3
2   8   5
7   0   6

current state:
4   1   3
7   2   5
8   0   6

current state:
1   3   5
4   0   2
7   8   6

current state:
1   3   5
4   2   6
7   8   0

current state:
0   2   3
1   4   5
7   8   6

current state:
1   2   3
7   4   5
0   8   6

current state:
1   2   0
4   5   3
7   8   6

DFS:
current state:
1   2   3
4   5   6
7   8   0

solved  
Execution time:  0.05716480000000024  
Number of states visited:  67  

## Results for 24 Piece Puzzle
start = [[6, 18, 12, 0, 24], [13, 7, 9, 2, 17], [1, 23, 8, 14, 11], [19, 22, 3, 15, 16], [21, 5, 4, 10, 20]]

We ran both overnight without reaching a solution. The first few moves for each algorythm is included below. 

## Breadth-First Search

current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   0
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   0
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   0   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   0   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20

current state:
6   0   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20
 
current state:
6   18   12   24   17
13   7   9   2   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   0   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20

current state:
0   6   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   7   18   12   24
13   0   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   0   7   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   2   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   8   2   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   0   2
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   0   7   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   2   24
13   7   12   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state: 
6   18   12   2   24
13   7   8   9   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   0
13   7   9   17   24
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   0   8   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   11   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   0   16
21   5   4   10   20

current state:
0   6   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   7   18   12   24
13   0   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   0   7   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   2   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   8   2   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   0   2
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   0   7   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   2   24
13   7   12   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   8   9   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   0
13   7   9   17   24
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   0   8   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   11   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   0   16
21   5   4   10   20

current state:
13   6   18   12   24
0   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state: 
6   7   18   12   24
0   13   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   7   18   12   24
13   9   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   7   18   12   24
13   23   9   2   17
1   0   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
0   13   7   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   0   9   12   24
13   18   7   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   23   7   2   17
1   0   8   14   11
19   22   3   15   16
21   5   4   10   20

## Depth-First Seacrh

current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   0   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   0
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   0
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   0   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   0   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20

current state:
6   0   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20
 
current state:
6   18   9   12   24
13   7   0   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   0   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   0
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   0   11
19   22   3   15   16
21   5   4   10   20

current state:
0   6   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   7   18   12   24
13   0   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   0   7   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   2   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   8   2   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   0   2
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   0   7   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   2   24
13   7   12   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   8   9   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   0
13   7   9   17   24
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   0   8   11
19   22   3   15   16
21   5   4   10   20

current state: 
6   18   12   2   24
13   7   9   14   17
1   23   8   11   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   15   11
19   22   3   0   16
21   5   4   10   20

current state:
0   6   18   12   24
13   7   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   7   18   12   24
13   0   9   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   0   7   2   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   2   0   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   9   12   24
13   7   8   2   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   0   2
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   24   17
13   7   9   2   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state: 
6   18   12   2   24
13   0   7   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   0   2   24
13   7   12   9   17
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   8   9   17
1   23   0   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   0
13   7   9   17   24
1   23   8   14   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   17   11
1   23   8   14   0
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   0   8   11
19   22   3   15   16
21   5   4   10   20

current state:
6   18   12   2   24
13   7   9   14   17
1   23   8   11   0
19   22   3   15   16
21   5   4   10   20
