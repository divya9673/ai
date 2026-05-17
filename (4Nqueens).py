N = int(input("Enter value of N: "))

board = [["." for i in range(N)] for j in range(N)]

def is_safe(row, col):

    # Check upper column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    # All queens placed
    if row == N:
        for r in board:
            print(" ".join(r))
        print()
        return

    for col in range(N):

        if is_safe(row, col):

            board[row][col] = "Q"

            solve(row + 1)

            # Backtrack
            board[row][col] = "."


solve(0)





#1. Start the program.
#2. Input the value of N for the chessboard size.
#3. Create an empty N × N chessboard.
#4. Define a function to check whether a queen can be placed safely.
#5. Check the column, left diagonal, and right diagonal for another queen.
#6. If the position is safe, place the queen.
#7. Recursively place queens in the next row.
#8. If all queens are placed, print the solution.
#9. If a position leads to no solution, remove the queen (backtracking).
#10. Repeat until all possible solutions are found.
#11. End the program.





#This code solves the N-Queen Problem using the Backtracking technique.
#
#* First, the user enters the size of the chessboard N.
#* An empty N × N board is created.
#* The is_safe() function checks whether a queen can be placed safely by checking:
#    * the same column,
#    * left diagonal,
#    * right diagonal.
#* The solve() function places queens row by row.
#* If a safe position is found, the queen is placed and the next row is checked recursively.
#* If no valid position is possible, the algorithm removes the previously placed queen (backtracking) and tries another position.
#* When all queens are placed successfully, the solution is printed.
