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




#Enter number of vertices:
#4
#
#Enter number of edges:
#5
#
#Enter edges in format: start end weight
#
#A B 1
#A C 4
#B C 2
#B D 5
#C D 3
#
#
#Edges in Minimum Spanning Tree:
#A - B = 1
#B - C = 2
#C - D = 3
#
#Minimum Cost = 6


#Algorithm
#
#1. Start the program.
#2. Input the number of vertices and edges.
#3. Read all edges with their weights.
#4. Store the edges in a list.
#5. Sort all edges in increasing order of weight.
#6. Initialize each vertex as its own parent.
#7. Select the edge with minimum weight.
#8. Check whether the selected edge forms a cycle using the find function.
#9. If no cycle is formed, add the edge to the Minimum Spanning Tree (MST).
#10. Union the connected vertices.
#11. Add the edge weight to the total cost.
#12. Repeat until all required edges are selected.
#13. Display the MST edges and minimum cost.
#14. End the program.
#
#⸻
#
#Why it is a Greedy Approach
#
#This code implements Kruskal’s Algorithm, which is a Greedy Algorithm because:
#
#* At every step, it chooses the minimum weight edge available.
#* It makes the best local choice without considering future choices.
#* Once an edge is selected, the decision is not changed.
#* The algorithm keeps selecting the smallest edges while avoiding cycles.
#* This greedy strategy helps form the Minimum Spanning Tree with minimum total cost.
