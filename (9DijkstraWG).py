import heapq

graph = {}

# Add edge function
def add_edge(u, v, w):

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append((v, w))
    graph[v].append((u, w))


# Dijkstra function
def dijkstra(start):

    pq = []

    heapq.heappush(pq, (0, start))

    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    while pq:

        dist, current = heapq.heappop(pq)

        print("Visited:", current)

        for neighbor, weight in graph[current]:

            new_distance = dist + weight

            if new_distance < distance[neighbor]:

                distance[neighbor] = new_distance

                heapq.heappush(pq,
                               (new_distance, neighbor))

    return distance


# Input section
n = int(input("Enter number of edges: "))

print("Enter edges (u v weight):")

for i in range(n):

    u, v, w = input().split()

    add_edge(u, v, int(w))


start = input("Enter starting node: ")

result = dijkstra(start)

print("\nShortest Distances:")

for node in result:
    print(start, "to", node, "=", result[node])
    
    
    
    
    
    
# Enter number of edges: 5
#Enter edges (u v weight):
#A B 4
#A C 2
#B C 5
#B D 10
#C D 3
#Enter starting node: A
#Visited: A
#Visited: C
#Visited: B
#Visited: D
#
#Shortest Distances:
#A to A = 0
#A to B = 4
#A to C = 2
#A to D = 5
#





#1. Start the program.
#2. Create an empty graph.
#3. Input the number of edges.
#4. Read each edge with source, destination, and weight.
#5. Add edges to the graph.
#6. Input the starting node.
#7. Initialize all node distances as infinity.
#8. Set the starting node distance as 0.
#9. Insert the starting node into the priority queue.
#10. Remove the node with minimum distance from the queue.
#11. Visit all neighboring nodes.
#12. Update the distance if a shorter path is found.
#13. Insert updated nodes into the priority queue.
#14. Repeat until the queue becomes empty.
#15. Display the shortest distances from the starting node.
#16. End the program.
