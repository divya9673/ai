from queue import PriorityQueue

# Graph representation
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 2},
    'B': {'C': 5},
    'C': {'G': 1},
    'G': {}
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'G': 0
}


def a_star(start, goal):

    pq = PriorityQueue()

    pq.put((0, start))

    cost = {start: 0}

    while not pq.empty():

        current = pq.get()[1]

        print("Visited:", current)

        # Goal reached
        if current == goal:
            print("Goal Reached")
            return cost[current]

        # Explore neighbors
        for neighbor, weight in graph[current].items():

            new_cost = cost[current] + weight

            # Better path found
            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                priority = new_cost + heuristic[neighbor]

                pq.put((priority, neighbor))

    return -1


result = a_star('S', 'G')

print("Minimum Cost =", result)