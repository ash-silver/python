import sys
input = sys.stdin.readline

board = list(input().rstrip())
i = 0


while i <= (len(board) - 1):
    if board[i] == ".":
        i += 1
    elif board[i:(i + 4)] == list("XXXX"):
        board[i], board[i + 1], board[i + 2], board[i + 3] = 'A', 'A', 'A', 'A'
        i += 4
    elif board[i:(i + 2)] == list("XX"):
        board[i], board[i + 1] = 'B', 'B'
        i += 2
    else:
        board = -1
        break
if board == -1:
    print(board)
else:
    for i in board:
        print(i, end ="")
