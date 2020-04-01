#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : Madhura Bartakke mabartak
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
# Initializing visited array
visited=[]

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]
    
#IUB_map=parse_map('C:\\Users\\Madhura\\Downloads\\mabartak-a0-master\\mabartak-a0-master\\map.txt')


def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
# Adding a positional parameter for each direction
def moves(map, row, col):
    moves=((row+1,col,'S'), (row-1,col,'N'), (row,col-1,'W'), (row,col+1,'E'))
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe=[(you_loc,0,'')]
    
    
    while fringe:
        # First in First out element from fringe
        (curr_move, curr_dist, path)=fringe.pop(0)
        # Appending value of current move to visited array 
        visited.append(curr_move[0:2])
        for move in moves(IUB_map, curr_move[0],curr_move[1]):
            # Condition if move is in visited
            if move[0:2] not in visited:
                if IUB_map[move[0]][move[1]]=="@":
                    # Adding current distance value and path of directions
                    return str(curr_dist+1)+' '+path+move[2]
                else:
                    # Adding direction as positional parameter
                    fringe.append((move[0:2], curr_dist + 1,path+move[2]))
                

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    solution = search1(IUB_map)
    print("Here's the solution I found:")
    print(solution if solution else 'INF')

