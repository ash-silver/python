import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = []
answerChess = []
minimum = 64

# 정답 체스판 만들기
white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

whiteChess = [0] * 8
blackChess = [0] * 8

for i in range(0, 8, 2):
    whiteChess[i] = white
    blackChess[i] = black
for i in range(1, 8, 2):
    whiteChess[i] = black
    blackChess[i] = white

def change(i, k):
    global chess
    global count
    global answerChess
    a = 0
    for g in range(i, i + 8):
        if chess[g] != answerChess[a]:
            b = 0
            for h in range(k, k + 8):
                if chess[g][h] != answerChess[a][b]:
                    count += 1
                b += 1
        a += 1
    
    return count
        
# 체스 판 입력 받기
for i in range(n):
    chess.append(list(input().rstrip()))

# 시작점 위치 정하기
for i in range(0, n - 7):
    for k in range(0, m - 7):
        if chess[i][k] == 'W':
            answerChess = whiteChess
        else : 
            answerChess = blackChess
        
        count = 0
        count = change(i, k)
        count = min(count, abs(64 - count))
        minimum = min(minimum, count)

print(minimum)