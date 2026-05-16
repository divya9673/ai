graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    v = input("Enter vertex: ")
    graph[v] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    a, b = input("Enter edge: ").split()
    graph[a].append(b)
    graph[b].append(a)

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for i in graph[node]:
            dfs(i)

from collections import deque

def bfs(start):
    visited = set()
    q = deque()

    visited.add(start)
    q.append(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                q.append(i)

start = input("Enter starting vertex: ")

print("DFS Traversal:")
dfs(start)

print("\nBFS Traversal:")
bfs(start)


