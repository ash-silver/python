import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
gDo = [0] * n

answerTime = 987654321
answerHeight = -1
allBlock = b

for i in range(0, n):
    gDo[i] = list(map(int, input().split()))
    allBlock += sum(gDo[i])

maximum = max(max(gDo))
minimum = min(min(gDo))

def sol(height):
    global answerHeight
    global answerTime
    inventory = b
    time = 0
    for i in range(0, n):
        for k in range(0, m):
            if gDo[i][k] >= height:
                tmp = gDo[i][k] - height
                inventory += tmp
                time += tmp * 2
            else:
                tmp = height - gDo[i][k]
                inventory -= tmp
                time += tmp
    if inventory >= 0:
        if time <= answerTime:
            answerTime = time
            answerHeight = height


for i in range(minimum, maximum + 1):
    if allBlock - (i * n * m) < 0:
        continue
    sol(i)
    
print(answerTime, answerHeight)
