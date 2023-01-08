import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())
answer = 1
cnt = 0

if n > 0:
    scoreLi = list(map(int, input().split()))
else:
    scoreLi = []

for i in range(0, len(scoreLi)):
    if scoreLi[i] > score:
        answer += 1
    elif scoreLi[i] == score:
        answer = answer
    else:
        break
    cnt += 1
if cnt >= p:
    answer = -1
if answer > p:
    answer = -1
print(answer)