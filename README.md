**Assignment 0**

**Problem 1**

**Objective**

-   The goal is to find the shortest path between where you are and Luddy Hall
    using IUB_map

-   You are allowed to move one sidewalk square at a time in one of four
    principal compass directions.

-   The program should find the shortest distance between the two points and
    then output a string of letters (compass directions) indicating that
    solution.

**Working**

-   At first IUB_map function stores the initial position (ie.\#) in the fringe
    along with the current distance from the start (ie 0).

-   **Original code** : the original code popped the element (ie tuple) from the
    fringe in stack manner (ie. Last in first out)

-   **Revised code** : while in the revise code the first tuple is popped out of
    the fringe.

    (curr_move, curr_dist, path)=**fringe.pop(0)**

-   Now in the while loop it checks whether the current tuple (row,column)
    encounters the end condition. If it does not encounter the end condition,
    then it appends the fringe.

-   **Original code** : this code doesn’t have a count for all the visited node
    and hence in the output it was checking for the same condition again and
    going into the infinite loop. It didn’t have the storage of the path.

-   **Revised code** : I introduced a list named visited, where I stored all the
    visited nodes. The next condition that it checked was if the current move
    was not in the visited, then it would check for both the condition. I also
    added storage of the path by being the third element in the tuple. The
    revised code is as follows:-

    while fringe:

    (curr_move, curr_dist, path)=fringe.pop(**0**)

    **visited.append(curr_move[0:2])**

    for move in moves(IUB_map,curr_move[0],curr_move[1]):

    **if move[0:2] not in visited:**

    if IUB_map[move[0]][move[1]]=="\@":

    return curr_dist+1,**path+move[2]**

    else:

    fringe.append((move**[0:2]**, curr_dist + 1,**path+move[2]**))

-   To define the directions and print the path traversed, I named third tuple
    as the direction for eg. (row+1,col) corresponds to the South direction and
    hence third tuple for the direction will be a string ‘S’. Secondly, the
    current moves direction (ie third element) in the tuple is getting appended
    in the return statement.

    moves=((row+1,col,'**S**'), (row-1,col,'**N**'), (row,col-1,'**W**'),
    (row,col+1,'**E**'))

**Problems faced**

-   The code used to go in infinite loop because the node which were already
    visited were revisited in the next iteration.

-   Even after defining the visited list, the code used to pop out just one
    child of the parent even if the parent had more than one child.

-   Hence because of this problem the code took a longer path and gave 18 as
    solution.

**Assumptions**

-   If it has two optimal paths, it takes the path of the direction which is
    defined first in the moves.

**Design decisions**

-   Created a list called a visited.

-   Named all the moves as ‘S’, ‘N’, ‘E’, ‘W’ respectively.

-   Added third element in the tuple to store the path.

**Valid State**

Valid State consists of all the states which is on the sidewalk (ie ‘.’ , ‘\#’ ,
‘\@’) and not in the obstruction.

**Successor function**

Successor function gives all the valid child states for any given point.

**Cost Function**

Number of steps to reach the goal : 16

**Goal state**

Goal state is the state when you find the shortest path from current position to
luddy hall.

....&&&

.&&&...

....&..

.&.&...

.&.&.&.

\#&...&\@

**Initial state**

....&&&

.&&&...

....&..

.&.&...

.&.&.&.

\#&...&\@

**Problem 2**

**Objective**

-   The goal of the program to arrange your friends on the IU campus such that
    no two of your friends can see one another.

-   Two friends can see each other if they are on either the same row or column
    of the map, and there are no buildings between them.

-   Your friends can only be positioned on sidewalks. (Any building including
    Luddy Hall obscures the view, but you do not.)

-   The program should output to the screen (in the last lines of its output) a
    new version of the map but with friends' locations marked with letters F.

**Working**

-   Hide.py uses DFS algorithm.

-   My solution includes traversing through the row and column of the
    co-ordinate selected to place a friend.

-   It checks the position if it is ‘.’ (ie. Sidewalk)

-   After it finds a ‘.’, it checks two conditions in all the 4 directions 1.If
    there’s a friend placed, the position is discarded. 2. If it encounters ‘&’
    or ‘\@’, it stops checking.

**Problems faced**

For checking a column above the position, the elements in the list of list had
to be checked in reverse order.

**Design decisions**

For the above problem faced, I retrieved each element in the list of list.
Created a list of those elements and finally reversed the list.

**Valid State**

Valid State is state where a friend could be placed that is on the sidewalk and
not on the current row as well as current column.

**Successor function**

Successor function is a function where position on the board is checked for its
validity.

**Cost function**

Cost function is the number of steps for a friend to be placed so that no other
friend sees each other.

**Goal state**

Goal state is the state where all the friends are placed where no two friends
can see each other.

**Initial state**

Initial state is a state where no friends are placed in the map.

....&&&

.&&&...

....&..

.&.&...

.&.&.&.

\#&...&\@
