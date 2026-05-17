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