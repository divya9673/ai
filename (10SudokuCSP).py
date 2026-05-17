board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],

    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],

    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def print_board(board):

    for row in board:
        print(row)


def find_empty(board):

    for i in range(9):

        for j in range(9):

            if board[i][j] == 0:
                return (i, j)

    return None


def is_valid(board, num, row, col):

    # check row
    for j in range(9):

        if board[row][j] == num:
            return False

    # check column
    for i in range(9):

        if board[i][col] == num:
            return False

    # check 3x3 box

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):

        for j in range(start_col, start_col + 3):

            if board[i][j] == num:
                return False

    return True


def solve(board):

    empty = find_empty(board)

    # no empty cell means solved
    if empty is None:
        return True

    row, col = empty

    # try numbers 1 to 9
    for num in range(1, 10):

        if is_valid(board, num, row, col):

            board[row][col] = num

            # recursive call
            if solve(board):
                return True

            # backtrack
            board[row][col] = 0

    return False


solve(board)

print_board(board)






#1. Start the program.
#2. Define the Sudoku board with empty cells represented by 0.
#3. Find an empty cell in the board.
#4. If no empty cell exists, the Sudoku is solved.
#5. Try placing numbers from 1 to 9 in the empty cell.
#6. Check whether the number is valid in the row, column, and 3×3 box.
#7. If the number is valid, place it in the cell.
#8. Recursively solve the remaining Sudoku board.
#9. If the solution fails, remove the number (backtracking).
#10. Repeat the process until the board is solved.
#11. Print the solved Sudoku board.
#12. End the program.






#This code solves a Sudoku puzzle using the Backtracking Algorithm.
#
#* The Sudoku board is stored as a 9×9 matrix where 0 represents empty cells.
#* The find_empty() function searches for an empty position in the board.
#* The is_valid() function checks whether a number can be placed safely by verifying:
#    * the row,
#    * the column,
#    * and the 3×3 box.
#* The solve() function tries numbers from 1 to 9 in the empty cell.
#* If a valid number is found, it is placed on the board and the function calls itself recursively to solve the remaining puzzle.
#* If no number works, the algorithm removes the previously placed number (backtracking) and tries another number.
#* When all cells are filled correctly, the solved Sudoku board is printed.
