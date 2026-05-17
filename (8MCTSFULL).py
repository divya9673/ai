import random
import math

board = [" " for _ in range(9)]

def show(b):
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print()

def win(b, p):
    c = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for x in c:
        if b[x[0]] == b[x[1]] == b[x[2]] == p:
            return True
    return False

def full(b):
    return " " not in b

def moves(b):
    return [i for i in range(9) if b[i] == " "]

def minimax(b, d, maxi):
    if win(b, "O"):
        return 1
    if win(b, "X"):
        return -1
    if full(b):
        return 0

    if maxi:
        best = -100
        for i in moves(b):
            b[i] = "O"
            val = minimax(b, d+1, False)
            b[i] = " "
            best = max(best, val)
        return best
    else:
        best = 100
        for i in moves(b):
            b[i] = "X"
            val = minimax(b, d+1, True)
            b[i] = " "
            best = min(best, val)
        return best

def best_minimax(b):
    best = -100
    move = -1
    for i in moves(b):
        b[i] = "O"
        val = minimax(b, 0, False)
        b[i] = " "
        if val > best:
            best = val
            move = i
    return move

def alphabeta(b, d, a, beta, maxi):
    if win(b, "O"):
        return 1
    if win(b, "X"):
        return -1
    if full(b):
        return 0

    if maxi:
        best = -100
        for i in moves(b):
            b[i] = "O"
            val = alphabeta(b, d+1, a, beta, False)
            b[i] = " "
            best = max(best, val)
            a = max(a, best)
            if beta <= a:
                break
        return best
    else:
        best = 100
        for i in moves(b):
            b[i] = "X"
            val = alphabeta(b, d+1, a, beta, True)
            b[i] = " "
            best = min(best, val)
            beta = min(beta, best)
            if beta <= a:
                break
        return best

def best_alpha(b):
    best = -100
    move = -1
    for i in moves(b):
        b[i] = "O"
        val = alphabeta(b, 0, -100, 100, False)
        b[i] = " "
        if val > best:
            best = val
            move = i
    return move

class Node:
    def __init__(self, b, p, parent=None):
        self.board = b[:]
        self.player = p
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.move = None

    def expand(self):
        for i in moves(self.board):
            nb = self.board[:]
            nb[i] = self.player
            np = "X" if self.player == "O" else "O"
            child = Node(nb, np, self)
            child.move = i
            self.children.append(child)

    def select(self):
        best = -1
        node = None
        for c in self.children:
            if c.visits == 0:
                return c
            ucb = (c.wins / c.visits) + math.sqrt(2 * math.log(self.visits) / c.visits)
            if ucb > best:
                best = ucb
                node = c
        return node

def simulate(b, p):
    temp = b[:]
    cur = p

    while True:
        if win(temp, "O"):
            return "O"
        if win(temp, "X"):
            return "X"
        if full(temp):
            return "D"

        m = random.choice(moves(temp))
        temp[m] = cur
        cur = "X" if cur == "O" else "O"

def mcts(b, p, n=500):
    root = Node(b, p)
    root.expand()

    for _ in range(n):
        node = root

        while node.children:
            node = node.select()

        if not win(node.board, "X") and not win(node.board, "O") and not full(node.board):
            node.expand()
            if node.children:
                node = random.choice(node.children)

        result = simulate(node.board, node.player)

        while node:
            node.visits += 1
            if result == "O":
                node.wins += 1
            node = node.parent

    best = max(root.children, key=lambda x: x.visits)
    return best.move

print("1 Minimax")
print("2 Alpha Beta")
print("3 MCTS")

ch = int(input("Choice: "))

while True:
    show(board)

    x = int(input("Enter position 0-8: "))
    if board[x] != " ":
        continue

    board[x] = "X"

    if win(board, "X"):
        show(board)
        print("You Win")
        break

    if full(board):
        show(board)
        print("Draw")
        break

    if ch == 1:
        ai = best_minimax(board)
    elif ch == 2:
        ai = best_alpha(board)
    else:
        ai = mcts(board, "O")

    board[ai] = "O"

    if win(board, "O"):
        show(board)
        print("Computer Wins")
        break

    if full(board):
        show(board)
        print("Draw")
        break
        
        
        
        
        
#1. Start the program.
#2. Create an empty Tic-Tac-Toe board.
#3. Display the algorithm choices: Minimax, Alpha-Beta, or MCTS.
#4. Take the user’s choice for AI algorithm.
#5. Display the game board.
#6. Take the player’s move as input.
#7. Check if the move is valid.
#8. Place "X" for the player’s move.
#9. Check if the player wins or if the board is full.
#10. If the game is not over, generate the computer’s move using the selected algorithm.
#11. Place "O" for the computer’s move.
#12. Check if the computer wins or if the board is full.
#13. Repeat the process until the game ends.
#14. Display the final result (Win/Loss/Draw).
#15. End the program.
