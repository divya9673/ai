from collections import deque 
 
graph = {} 
 
def add_edge(u, v): 
    if u not in graph: 
        graph[u] = [] 
    if v not in graph: 
        graph[v] = [] 
 
    graph[u].append(v) 
    graph[v].append(u) 
 
 
def BFS(graph, start): 
    visited = set() 
    queue = deque([start]) 
 
    visited.add(start) 
 
    while queue: 
 
        vertex = queue.popleft() 
        print(vertex, end=" ") 
 
        for neighbor in graph[vertex]: 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor) 
 
 
print("Enter number of edges:") 
n = int(input()) 
 
print("Enter edges (u v):") 
for _ in range(n): 
    u, v = map(int, input().split()) 
    add_edge(u, v) 
 
print("Enter starting vertex for BFS:") 
start = int(input()) 
 
print("BFS Traversal:") 
BFS(graph, start)









#1. Start the program.
#2. Create an empty graph.
#3. Input the number of edges.
#4. Read each edge and add it to the graph.
#5. Input the starting vertex.
#6. Create an empty visited set.
#7. Create a queue and insert the starting vertex into it.
#8. Mark the starting vertex as visited.
#9. Repeat until the queue becomes empty:
#    * Remove a vertex from the front of the queue.
#    * Print the vertex.
#    * Visit all unvisited adjacent vertices.
#    * Mark them as visited and add them to the queue.
#10. End the program.












#from collections import deque
#
#* Imports deque from the collections module.
#* deque is used as a queue for BFS traversal.
#
#⸻
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
#* Checks whether vertex u exists in the graph.
#* If not, creates an empty list for it.
#
#⸻
#
#    if v not in graph:
#        graph[v] = []
#
#* Checks whether vertex v exists in the graph.
#* If not, creates an empty list for it.
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
#def BFS(graph, start):
#
#* Defines the BFS traversal function.
#
#⸻
#
#    visited = set()
#
#* Creates an empty set to store visited vertices.
#
#⸻
#
#    queue = deque([start])
#
#* Creates a queue and inserts the starting vertex into it.
#
#⸻
#
#    visited.add(start)
#
#* Marks the starting vertex as visited.
#
#⸻
#
#    while queue:
#
#* Runs the loop until the queue becomes empty.
#
#⸻
#
#        vertex = queue.popleft()
#
#* Removes the front element from the queue and stores it in vertex.
#
#⸻
#
#        print(vertex, end=" ")
#
#* Prints the current vertex.
#
#⸻
#
#        for neighbor in graph[vertex]:
#
#* Loops through all adjacent vertices of the current vertex.
#
#⸻
#
#            if neighbor not in visited:
#
#* Checks whether the adjacent vertex has already been visited.
#
#⸻
#
#                visited.add(neighbor)
#
#* Marks the adjacent vertex as visited.
#
#⸻
#
#                queue.append(neighbor)
#
#* Adds the unvisited neighbor to the queue.
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
#* Displays a message asking the user to enter edges.
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
#* Takes two integers as input representing an edge.
#
#⸻
#
#    add_edge(u, v)
#
#* Adds the edge to the graph.
#
#⸻
#
#print("Enter starting vertex for BFS:")
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
#print("BFS Traversal:")
#
#* Displays the BFS traversal heading.
#
#⸻
#
#BFS(graph, start)
#
#* Calls the BFS function to start traversal from the given vertex.
