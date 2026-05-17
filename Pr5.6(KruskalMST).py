def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parent[find(parent, a)] = find(parent, b)

v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges in format: start end weight")

for i in range(e):
    u, v1, w = input().split()
    edges.append((int(w), u, v1))

edges.sort()

parent = {}

for w, u, v1 in edges:
    parent[u] = u
    parent[v1] = v1

cost = 0

print("Edges in Minimum Spanning Tree:")

for w, u, v1 in edges:
    if find(parent, u) != find(parent, v1):
        union(parent, u, v1)
        print(u, "-", v1, "=", w)
        cost += w

print("Minimum Cost =", cost)