graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)


def DFS(graph, start):
    visited = set()
    DFS_recursive(graph, start, visited)


def DFS_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            DFS_recursive(graph, neighbor, visited)


print("Enter number of edges:")
n = int(input())

print("Enter edges (u v):")
for _ in range(n):
    u, v = map(int, input().split())
    add_edge(u, v)

print("Enter starting vertex for DFS:")
start = int(input())

print("DFS Traversal:")
DFS(graph, start)









#1. Start the program.
#2. Create an empty graph.
#3. Input the number of edges.
#4. Read each edge and add it to the graph.
#5. Input the starting vertex.
#6. Create an empty visited set.
#7. Mark the starting vertex as visited and print it.
#8. Visit all unvisited adjacent vertices recursively using DFS.
#9. Repeat until all reachable vertices are visited.
#10. End the program.
#
#
#
#graph = {}
#
#* Creates an empty dictionary to store the graph using an adjacency list.
#
#⸻
#
#def add_edge(u, v):
#
#* Defines a function to add an edge between vertices u and v.
#
#⸻
#
#    if u not in graph:
#        graph[u] = []
#
#* Checks if vertex u is not already in the graph.
#* If not present, creates an empty list for u.
#
#⸻
#
#    if v not in graph:
#        graph[v] = []
#
#* Checks if vertex v is not already in the graph.
#* If not present, creates an empty list for v.
#
#⸻
#
#    graph[u].append(v)
#
#* Adds vertex v to the adjacency list of u.
#
#⸻
#
#    graph[v].append(u)
#
#* Adds vertex u to the adjacency list of v.
#* This makes the graph undirected.
#
#⸻
#
#def DFS(graph, start):
#
#* Defines the DFS function.
#
#⸻
#
#    visited = set()
#
#* Creates an empty set to keep track of visited vertices.
#
#⸻
#
#    DFS_recursive(graph, start, visited)
#
#* Calls the recursive DFS function starting from the given vertex.
#
#⸻
#
#def DFS_recursive(graph, vertex, visited):
#
#* Defines the recursive DFS function.
#
#⸻
#
#    visited.add(vertex)
#
#* Marks the current vertex as visited.
#
#⸻
#
#    print(vertex, end=" ")
#
#* Prints the current vertex.
#
#⸻
#
#    for neighbor in graph[vertex]:
#
#* Loops through all adjacent vertices of the current vertex.
#
#⸻
#
#        if neighbor not in visited:
#
#* Checks if the adjacent vertex has not been visited.
#
#⸻
#
#            DFS_recursive(graph, neighbor, visited)
#
#* Recursively visits the unvisited neighbor.
#
#⸻
#
#print("Enter number of edges:")
#
#* Displays a message asking for the number of edges.
#
#⸻
#
#n = int(input())
#
#* Takes the number of edges as input.
#
#⸻
#
#print("Enter edges (u v):")
#
#* Displays a message asking for edge inputs.
#
#⸻
#
#for _ in range(n):
#
#* Runs the loop n times to input all edges.
#
#⸻
#
#    u, v = map(int, input().split())
#
#* Takes two integers as vertices of an edge.
#
#⸻
#
#    add_edge(u, v)
#
#* Adds the edge to the graph.
#
#⸻
#
#print("Enter starting vertex for DFS:")
#
#* Displays a message asking for the starting vertex.
#
#⸻
#
#start = int(input())
#
#* Takes the starting vertex as input.
#
#⸻
#
#print("DFS Traversal:")
#
#* Displays the DFS traversal heading.
#
#⸻
#
#DFS(graph, start)
#
#* Calls the DFS function to start traversal.
