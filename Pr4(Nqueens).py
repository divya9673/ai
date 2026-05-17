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