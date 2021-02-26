from array import *
import random
import time

sol = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
start = [[6, 18, 12, 0, 24], [13, 7, 9, 2, 17], [1, 23, 8, 14, 11], [19, 22, 3, 15, 16], [21, 5, 4, 10, 20]]

size = 5

#check if state is solved
def checkifsolved(state):
    count = 1
    #for each val in matrix
    for x in range(size):
        for y in range(size):
            #if vals are not in order
            if state[x][y] != count:
                #if we're at the last val return true, otherwise false
                if count == size*size:
                    return True;
                else:
                    return False;
            count = count + 1

def copy(m):
    copy = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for x in range(size):
        for y in range(size):
            copy[x][y] = m[x][y]
    return copy

def equals(a, b):
    for x in range(size):
        for y in range(size):
            if a[x][y] != b[x][y]:
                return False;
    return True;

def findMoves(state):
    moves = []
    
    #find 0
    r0 = 0
    c0 = 0
    for x in range(size):
        for y in range(size):
            if state[x][y] == 0:
                r0 = x
                c0 = y
                
    #find left
    #if col == 1, no left
    if c0 != 0:
        left = copy(state)
        #swap 0 and val to left
        temp = left[r0][c0 - 1]
        left[r0][c0 - 1] = 0
        left[r0][c0] = temp
        #add left to list
        moves.append(left)
    
    #find right
    #if col == 3, no right
    if c0 != size - 1:
        right = copy(state)
        #swap 0 and val to right
        temp = right[r0][c0 + 1]
        right[r0][c0 + 1] = 0
        right[r0][c0] = temp
        #add right to list
        moves.append(right)
    
    #find up
    #if row == 1, no up
    if r0 != 0:
        up = copy(state)
        #swap 0 and val above
        temp = up[r0 - 1][c0]
        up[r0 - 1][c0] = 0
        up[r0][c0] = temp
        #add up to list
        moves.append(up)
    
    #find down
    #if row == 3, no down
    if r0 != size - 1:
        down = copy(state)
        #swap 0 and val downwards
        temp = down[r0 + 1][c0]
        down[r0 + 1][c0] = 0
        down[r0][c0] = temp
        #add down to list
        moves.append(down)
    
    return moves;
    
def display(state):
    for x in range(size):
        print(state[x][0], " ", state[x][1], " ", state[x][2], " ", state[x][3], " ", state[x][4])
    print(" ")

def inlist(list, find):
    for item in list:
        if equals(item, find):
            return True
    return False
    
def bfs(init):
    #list for explored states
    explored = []
    #list for new states
    newstates = []
    #put initial state in explored
    explored.append(init)
    
    #timer
    totalTime = 0
    
    #add init to queue
    newstates.append(init)
    
    solved = False
    while not solved:
        #timer
        start = time.process_time()
        
        #display initial state
        print("current state: ")
        display(init)
        
        #fifo queue newstates
        
        #add next vertices to queue if they are not explored
        for move in findMoves(init):
            if not inlist(explored, move):
                newstates.insert(len(newstates), move)
        
        #change init to first item on newstates
        init = newstates.pop(0)
        #add init to explored list
        explored.append(init)
        
        #timer
        elapsed_time = time.process_time() - start
        totalTime = totalTime + elapsed_time
        print("time: ", totalTime)
        
        #number of moves
        print("moves: ", len(explored))
        
        #if current state = solution, exit loop
        if equals(init, sol):
            solved = True
    
def dfs(init):
    #list for explored states
    explored = []
    #list for new states
    newstates = []
    #put initial state in explored
    explored.append(init)
    
    #timer
    totalTime = 0
    
    #add init to queue
    newstates.append(init)
    
    solved = False
    while not solved:
        #timer
        start = time.process_time()
        
        #display initial state
        print("current state: ")
        display(init)
        
        #add next vertices to queue if they are not explored
        for move in findMoves(init):
            if not inlist(explored, move):
                newstates.insert(len(newstates), move)
        
        #change init to last item on newstates
        init = newstates.pop()
        #add init to explored list
        explored.append(init)
        
        #timer
        elapsed_time = time.process_time() - start
        totalTime = totalTime + elapsed_time
        print("time: ", totalTime)
        
        #number of moves
        print("moves: ", len(explored))
        
        #if current state = solution, exit loop
        if equals(init, sol):
            solved = True
"""
    #list for explored states
    explored = []
    #list for possible new states
    newstates = []
    #put initial state in explored list
    explored.append(init)
    
    #timer
    totalTime = 0
    
    solved = False;
    while not  solved:
        #timer
        start = time.process_time()
        
        #display initial state
        print("current state: ")
        display(init)
        
        #add new possible moves to newstates
        for move in findMoves(init):
            newstates.append(move)
            
        #make random new unexplored state the current state
        checked = False
        while not checked:
            #pick random state to explore next
            r = random.randint(0,(len(newstates) - 1))
            temp = newstates.pop(r)
            
            #if all states are explored, remove state to go back to previous one
            if len(newstates) == 0:
                explored.pop()
                init = explored.pop()
                explored.append(init)
                checked = True
            #if state is not explored, make that the current state
            if not inlist(explored, temp):
                init = temp
                checked = True
        
        #add new current state to explored list
        explored.append(init)
            
        #clear out newstates list
        newstates.clear()
        
        #timer
        elapsed_time = time.process_time() - start
        totalTime = totalTime + elapsed_time
        print("time: ", totalTime)
        
        #number of moves
        print("moves: ", len(explored))
        
        #if current state == solution, exit loop
        if equals(init, sol):
            solved = True
"""

choice = input("Type 1 for Depth First Search, Type 2 for Breadth First Search: ")
#print(choice)

if choice == '1':
    dfs(start)

if choice == '2':
    bfs(start)