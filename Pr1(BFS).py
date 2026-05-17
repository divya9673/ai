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