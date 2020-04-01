#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : Madhura Bartakke  mabartak
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys
# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]
    
#IUB_map=parse_map('C:\\Users\\Madhura\\Downloads\\mabartak-a0-master\\mabartak-a0-master\\map.txt')
# Reverses a list
def reverse(lst):
    lst.reverse()
    new_lst = lst
    return new_lst
# Checks the availability in current row and column
def possible(board, row, col):
    
    l=len(board)
    # Checks if its a sidewalk
    if board[row][col] == '.':
        
        # Checks for item in right of current position
        for item in board[row][col+1:-1]:
            if item == 'F':
                return False
            if item in '&@':
                break
        
        # Checks for item in left of current position
        for item in reverse(board[row][0:col]):
            if item == 'F':
                return False
            if item in '&@':
                break
            
        # Checks for item up of current position
        for i in range(row-1,-1,-1):
            if board[i][col] == 'F':
                return False
            if board[i][col] in '&@':
                break
            
        # Checks for item down of current position
        for i in range(row+1,l):
            if board[i][col] == 'F':
                return False
            if board[i][col] in '&@':
                break
            
        return True
    
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state and check availability
def successors(board):
    return [ add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if possible(board,r,c)]

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors( fringe.pop() ):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

#solution = solve(IUB_map)
#print(printable_board(solution) if solution else 'no solution found')
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")

