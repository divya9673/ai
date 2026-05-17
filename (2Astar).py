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

    parent = {start: None}

    while not pq.empty():

        current = pq.get()[1]

        print("Visited:", current)

        # Goal reached
        if current == goal:

            print("Goal Reached")

            # Find path
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("Optimal Path:", " -> ".join(path))

            return cost[goal]

        # Explore neighbors
        for neighbor, weight in graph[current].items():

            new_cost = cost[current] + weight

            # Better path found
            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost

                parent[neighbor] = current

                priority = new_cost + heuristic[neighbor]

                pq.put((priority, neighbor))

    return -1


result = a_star('S', 'G')

print("Minimum Cost =", result)



#Visited: S
#Visited: B
#Visited: A
#Visited: C
#Visited: G
#Goal Reached
#Optimal Path: S -> A -> C -> G
#Minimum Cost = 4









#1. Start the program.
#2. Create the graph and heuristic values.
#3. Insert the start node into the priority queue.
#4. Initialize cost and parent dictionaries.
#5. Remove the node with minimum priority from the queue.
#6. If the goal node is reached, display the optimal path and minimum cost.
#7. Otherwise, explore all neighboring nodes.
#8. Update cost, parent, and priority for better paths.
#9. Add updated nodes to the priority queue.
#10. Repeat until the goal is reached or the queue becomes empty.
#11. End the program.





#"""
#from queue import PriorityQueue
#
#* Imports PriorityQueue for selecting nodes with minimum priority.
#
#⸻
#
#graph = {
#    'S': {'A': 1, 'B': 4},
#    'A': {'C': 2},
#    'B': {'C': 5},
#    'C': {'G': 1},
#    'G': {}
#}
#
#* Creates the graph with edge costs.
#
#⸻
#
#heuristic = {
#    'S': 7,
#    'A': 6,
#    'B': 2,
#    'C': 1,
#    'G': 0
#}
#
#* Stores heuristic values for each node.
#
#⸻
#
#def a_star(start, goal):
#
#* Defines the A* search function.
#
#⸻
#
#    pq = PriorityQueue()
#
#* Creates an empty priority queue.
#
#⸻
#
#    pq.put((0, start))
#
#* Inserts the start node into the queue.
#
#⸻
#
#    cost = {start: 0}
#
#* Stores the cost to reach nodes.
#
#⸻
#
#    parent = {start: None}
#
#* Stores parent nodes for path tracing.
#
#⸻
#
#    while not pq.empty():
#
#* Runs until the queue becomes empty.
#
#⸻
#
#        current = pq.get()[1]
#
#* Removes the node with minimum priority.
#
#⸻
#
#        print("Visited:", current)
#
#* Prints the visited node.
#
#⸻
#
#        if current == goal:
#
#* Checks if the goal node is reached.
#
#⸻
#
#            path = []
#
#* Creates a list to store the path.
#
#⸻
#
#            while current is not None:
#
#* Traces the path backward.
#
#⸻
#
#                path.append(current)
#
#* Adds the node to the path.
#
#⸻
#
#                current = parent[current]
#
#* Moves to the parent node.
#
#⸻
#
#            path.reverse()
#
#* Reverses the path from start to goal.
#
#⸻
#
#            print("Optimal Path:", " -> ".join(path))
#
#* Displays the optimal path.
#
#⸻
#
#            return cost[goal]
#
#* Returns the minimum cost.
#
#⸻
#
#        for neighbor, weight in graph[current].items():
#
#* Visits all neighboring nodes.
#
#⸻
#
#            new_cost = cost[current] + weight
#
#* Calculates new path cost.
#
#⸻
#
#            if neighbor not in cost or new_cost < cost[neighbor]:
#
#* Checks for a better path.
#
#⸻
#
#                cost[neighbor] = new_cost
#
#* Updates the cost.
#
#⸻
#
#                parent[neighbor] = current
#
#* Stores the parent node.
#
#⸻
#
#                priority = new_cost + heuristic[neighbor]
#
#* Calculates priority:
#    f(n)=g(n)+h(n)
#
#⸻
#
#                pq.put((priority, neighbor))
#
#* Adds the neighbor to the queue.
#
#⸻
#
#result = a_star('S', 'G')
#
#* Calls the A* function.
#
#⸻
#
#print("Minimum Cost =", result)
#
#* Prints the minimum cost.
#"""
