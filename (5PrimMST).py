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



#Enter number of vertices:
#4
#
#Enter vertex: A
#Enter vertex: B
#Enter vertex: C
#Enter vertex: D
#
#Enter number of edges:
#5
#
#Enter first vertex: A
#Enter second vertex: B
#Enter weight: 1
#
#Enter first vertex: A
#Enter second vertex: C
#Enter weight: 4
#
#Enter first vertex: B
#Enter second vertex: C
#Enter weight: 2
#
#Enter first vertex: B
#Enter second vertex: D
#Enter weight: 5
#
#Enter first vertex: C
#Enter second vertex: D
#Enter weight: 3
#
#Enter starting vertex:
#A
#
#Minimum Spanning Tree:
#A - B = 1
#B - C = 2
#C - D = 3
#
#Total Cost: 6



#Algorithm
#
#1. Start the program.
#2. Input the number of vertices.
#3. Create an empty graph.
#4. Input the number of edges.
#5. Read each edge with its weight and store it in the graph.
#6. Input the starting vertex.
#7. Add the starting vertex to the visited list.
#8. Initialize total cost as 0.
#9. Find the minimum weight edge connecting a visited vertex to an unvisited vertex.
#10. Add the selected edge to the Minimum Spanning Tree (MST).
#11. Add the new vertex to the visited list.
#12. Add the edge weight to the total cost.
#13. Repeat until all vertices are visited.
#14. Display the Minimum Spanning Tree and total cost.
#15. End the program.
#
#⸻
#
#Why it is a Greedy Approach
#
#This code implements Prim’s Algorithm, which is a Greedy Algorithm because:
#
#* At every step, it selects the minimum weight edge available.
#* It always chooses the best local option to expand the tree.
#* Once an edge is selected, the decision is not changed.
#* The algorithm continues adding the smallest possible edge without forming cycles.
#* This greedy selection helps construct the Minimum Spanning Tree with minimum total cost.
