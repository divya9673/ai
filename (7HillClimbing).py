goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

def heuristic(state):
    count = 0

    for i in range(3):
        for j in range(3):

            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == 0:
                return i,j


def generate_neighbors(state):

    neighbors = []

    x,y = find_blank(state)

    moves = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    for dx,dy in moves:

        nx = x + dx
        ny = y + dy

        if nx >= 0 and nx < 3 and ny >= 0 and ny < 3:

            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = \
            new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


def hill_climbing(start):

    current = start

    while True:

        print("\nCurrent State:")
        for row in current:
            print(row)

        current_h = heuristic(current)

        print("Heuristic:", current_h)

        if current_h == 0:
            print("Goal Reached!")
            return

        neighbors = generate_neighbors(current)

        best_neighbor = None
        best_h = 999

        for neighbor in neighbors:

            h = heuristic(neighbor)

            if h < best_h:
                best_h = h
                best_neighbor = neighbor

        if best_h >= current_h:
            print("Stuck in Local Optimum")
            return

        current = best_neighbor


start = [
    [1,2,3],
    [4,0,6],
    [7,5,8]
]

hill_climbing(start)













#1. Start the program.
#2. Define the goal state of the puzzle.
#3. Define a heuristic function to count misplaced tiles.
#4. Find the blank space position in the puzzle.
#5. Generate neighboring states by moving the blank tile in possible directions.
#6. Set the start state as the current state.
#7. Calculate the heuristic value of the current state.
#8. If the heuristic value is 0, display “Goal Reached” and stop.
#9. Generate all neighboring states of the current state.
#10. Select the neighbor with the lowest heuristic value.
#11. If no better neighbor exists, display “Stuck in Local Optimum” and stop.
#12. Otherwise, update the current state with the best neighbor.
#13. Repeat the process until the goal state is reached.
#14. End the program.





#This code solves the 8-Puzzle Problem using the Hill Climbing Algorithm.
#
#* The goal variable stores the target puzzle arrangement.
#* The heuristic() function counts the number of misplaced tiles compared to the goal state.
#* The find_blank() function finds the position of the empty tile (0).
#* The generate_neighbors() function creates new puzzle states by moving the blank tile in possible directions (up, down, left, right).
#* The hill_climbing() function starts from the initial puzzle state and repeatedly:
#    * calculates the heuristic value,
#    * generates neighboring states,
#    * selects the neighbor with the lowest heuristic value.
#* If the heuristic becomes 0, the goal state is reached.
#* If no better neighboring state is found, the algorithm stops and displays “Stuck in Local Optimum”.
