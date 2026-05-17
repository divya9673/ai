board = [" " for _ in range(9)]

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def win(p):
    c = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for x in c:
        if board[x[0]] == board[x[1]] == board[x[2]] == p:
            return True
    return False

def full():
    return " " not in board

def minimax(maxi):
    if win("O"):
        return 1
    if win("X"):
        return -1
    if full():
        return 0

    if maxi:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                val = minimax(False)
                board[i] = " "
                best = max(best, val)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                val = minimax(True)
                board[i] = " "
                best = min(best, val)
        return best

def bestmove():
    best = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            val = minimax(False)
            board[i] = " "

            if val > best:
                best = val
                move = i

    return move

while True:
    show()

    x = int(input("Enter position 0-8: "))

    if board[x] != " ":
        continue

    board[x] = "X"

    if win("X"):
        show()
        print("You Win")
        break

    if full():
        show()
        print("Draw")
        break

    ai = bestmove()
    board[ai] = "O"

    if win("O"):
        show()
        print("Computer Wins")
        break

    if full():
        show()
        print("Draw")
        break