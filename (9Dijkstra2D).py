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


#Visited: 0 0
#Visited: 0 1
#Visited: 0 2
#Visited: 1 1
#Visited: 2 1
#Visited: 2 0
#Visited: 2 2
#The shortest path is: 4


#1. Start the program.
#2. Define the grid with blocked and open cells.
#3. Set the start position and goal position.
#4. Initialize all distances as infinity.
#5. Set the starting cell distance as 0.
#6. Create a priority queue and insert the starting cell.
#7. Remove the cell with minimum distance from the queue.
#8. If the goal cell is reached, return the shortest distance.
#9. Explore all valid neighboring cells (up, down, left, right).
#10. Check whether the neighboring cell is inside the grid and not blocked.
#11. Calculate the new distance for the neighboring cell.
#12. If the new distance is smaller, update the distance and insert the cell into the priority queue.
#13. Repeat until the queue becomes empty.
#14. Display the shortest path distance.
#15. End the program.



#This code finds the shortest path in a grid using Dijkstra’s Algorithm.
#
#* The grid contains:
#    * 0 → open path
#    * 1 → blocked cell
#* The starting point is (0,0) and the goal is the bottom-right cell.
#* A distance matrix stores the minimum distance to each cell.
#* A priority queue (heapq) is used to always select the cell with the shortest distance.
#* The algorithm explores neighboring cells in four directions:
#    * up,
#    * down,
#    * left,
#    * right.
#* If a neighboring cell is valid and gives a shorter path, its distance is updated and added to the queue.
#* The process continues until the goal cell is reached.
#* Finally, the shortest path length is printed.
