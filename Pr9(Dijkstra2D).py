import heapq

def dijkstra(grid):

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    distance = [[float('inf')] * cols for _ in range(rows)]

    distance[0][0] = 0

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    pq = []

    heapq.heappush(pq, (0, 0, 0))

    while pq:

        currentdist, x, y = heapq.heappop(pq)

        print("Visited:", x, y)

        if (x, y) == goal:
            return currentdist

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:

                newdist = currentdist + 1

                if newdist < distance[nx][ny]:

                    distance[nx][ny] = newdist

                    heapq.heappush(pq,
                                   (newdist, nx, ny))

    return -1


grid = [
    [0,0,0],
    [1,0,1],
    [0,0,0]
]

result = dijkstra(grid)

print("The shortest path is:", result)
