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