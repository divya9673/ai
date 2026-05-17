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