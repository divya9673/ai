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





#Enter number of vertices: 4
#Enter number of edges: 5
#Enter first vertex: A
#Enter second vertex: B
#Enter weight: 1
#Enter first vertex: A
#Enter second vertex: C
#Enter weight: 4
#Enter first vertex: B
#Enter second vertex: C
#Enter weight: 2
#Enter first vertex: B
#Enter second vertex: D
#Enter weight: 5
#Enter first vertex: C
#Enter second vertex: D
#Enter weight: 3
#Minimum Spanning Tree:
#A - B = 1
#B - C = 2
#C - D = 3
#Total Cost: 6



#Algorithm
#
#1. Start the program.
#2. Input the number of vertices and edges.
#3. Read all edges with their weights.
#4. Store the edges in a list.
#5. Sort all edges in increasing order of weight.
#6. Initialize each vertex as its own parent.
#7. Select the edge with minimum weight.
#8. Check whether adding the edge forms a cycle.
#9. If no cycle is formed, add the edge to the Minimum Spanning Tree (MST).
#10. Update the parent of connected vertices.
#11. Repeat until all required edges are selected.
#12. Display the Minimum Spanning Tree and total cost.
#13. End the program.
#
#⸻
#
#Why it is a Greedy Approach
#
#This code implements Kruskal’s Algorithm, which is a Greedy Algorithm because:
#
#* At every step, it chooses the minimum weight edge available.
#* It makes the locally optimal choice without considering future choices.
#* Once an edge is selected, the decision is not changed.
#* The algorithm continues selecting the smallest possible edges while avoiding cycles.
#* This greedy selection finally gives the Minimum Spanning Tree with minimum total cost.
