graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    graph[node] = []
    h[node] = int(input("Enter heuristic value: "))

e = int(input("Enter number of edges: "))

for i in range(e):
    a = input("Enter first node: ")
    b = input("Enter second node: ")
    c = int(input("Enter cost: "))

    graph[a].append((b, c))
    graph[b].append((a, c))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [start]
closed_list = []
g = {start: 0}
parent = {start: start}

while open_list:
    n = open_list[0]

    for v in open_list:
        if g[v] + h[v] < g[n] + h[n]:
            n = v

    if n == goal:
        path = []

        while parent[n] != n:
            path.append(n)
            n = parent[n]

        path.append(start)
        path.reverse()

        print("Path:", path)
        break

    for (m, cost) in graph[n]:
        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parent[m] = n
            g[m] = g[n] + cost

        else:
            if g[m] > g[n] + cost:
                g[m] = g[n] + cost
                parent[m] = n

                if m in closed_list:
                    closed_list.remove(m)
                    open_list.append(m)

    open_list.remove(n)
    closed_list.append(n)