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