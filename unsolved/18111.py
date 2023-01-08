from collections import Counter
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
gDo = []

answerTime = 987654321
answerHeight = -1
allBlock = b

for i in range(0, n):
    gDo += list(map(int, input().split()))
allBlock += sum(gDo)

maximum = max(gDo)
minimum = min(gDo)
counterGdo = Counter(gDo)

def sol(height):
    global answerHeight
    global answerTime
    time = 0
    for h, cnt in counterGdo.items():
        if h > height:
            time += 2 * (h - height) * cnt
        else:
            time += (height - h) * cnt
    if time < answerTime:
        answerTime = time
        answerHeight = height

for i in range(maximum, minimum -1, -1):
    if allBlock - (i * n * m) >= 0:
        sol(i)
    
print(answerTime, answerHeight)
