graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    v = input("Enter vertex: ")
    graph[v] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    a = input("Enter first vertex: ")
    b = input("Enter second vertex: ")
    w = int(input("Enter weight: "))

    graph[a].append([b, w])
    graph[b].append([a, w])

start = input("Enter source vertex: ")

dist = {}

for v in graph:
    dist[v] = 9999

dist[start] = 0

visited = []

while len(visited) < len(graph):

    min_node = None

    for v in graph:
        if v not in visited:
            if min_node is None or dist[v] < dist[min_node]:
                min_node = v

    visited.append(min_node)

    for node, weight in graph[min_node]:

        if dist[min_node] + weight < dist[node]:
            dist[node] = dist[min_node] + weight

print("Shortest Distances:")

for v in dist:
    print(v, "=", dist[v])
    
    
    
#  Enter number of vertices:
#4
#
#Enter vertex: A
#Enter vertex: B
#Enter vertex: C
#Enter vertex: D
#
#Enter number of edges:
#5
#
#Enter first vertex: A
#Enter second vertex: B
#Enter weight: 1
#
#Enter first vertex: A
#Enter second vertex: C
#Enter weight: 4
#
#Enter first vertex: B
#Enter second vertex: C
#Enter weight: 2
#
#Enter first vertex: B
#Enter second vertex: D
#Enter weight: 5
#
#Enter first vertex: C
#Enter second vertex: D
#Enter weight: 1
#
#Enter source vertex:
#A
#
#
#Shortest Distances:
#A = 0
#B = 1
#C = 3
#D = 4



#Algorithm
#
#1. Start the program.
#2. Input the number of vertices.
#3. Create the graph using an adjacency list.
#4. Input the number of edges.
#5. Read each edge with its weight and store it in the graph.
#6. Input the source vertex.
#7. Initialize all vertex distances as infinity (9999).
#8. Set the source vertex distance as 0.
#9. Create an empty visited list.
#10. Select the unvisited vertex with the minimum distance.
#11. Mark the selected vertex as visited.
#12. Update the distances of its neighboring vertices if a shorter path is found.
#13. Repeat until all vertices are visited.
#14. Display the shortest distances from the source vertex.
#15. End the program.
#
#⸻
#
#Why it is a Greedy Approach
#
#This code implements Dijkstra’s Algorithm, which is a Greedy Algorithm because:
#
#* At every step, it selects the unvisited vertex with the smallest distance.
#* It makes the best local choice without reconsidering previous decisions.
#* Once a node is marked visited, its shortest distance is considered final.
#* The algorithm repeatedly chooses the nearest node to build the shortest paths.
#* This greedy selection helps find the shortest distance efficiently.
