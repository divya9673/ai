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

start = input("Enter starting vertex: ")

visited = [start]

cost = 0

print("Minimum Spanning Tree:")

while len(visited) < len(graph):

    min_edge = None
    min_weight = 9999

    for v in visited:

        for node, weight in graph[v]:

            if node not in visited and weight < min_weight:
                min_weight = weight
                min_edge = [v, node]

    print(min_edge[0], "-", min_edge[1], "=", min_weight)

    cost += min_weight
    visited.append(min_edge[1])

print("Total Cost:", cost)