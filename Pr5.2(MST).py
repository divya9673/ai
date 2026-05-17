n = int(input("Enter number of vertices: "))

graph = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")
    w = int(input("Enter weight: "))

    graph.append([w, u, v])

graph.sort()

parent = {}

vertices = set()

for edge in graph:
    vertices.add(edge[1])
    vertices.add(edge[2])

for v in vertices:
    parent[v] = v

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

cost = 0

print("Minimum Spanning Tree:")

for w, u, v in graph:

    a = find(u)
    b = find(v)

    if a != b:
        print(u, "-", v, "=", w)
        cost += w
        parent[a] = b

print("Total Cost:", cost)