import sys
input = sys.stdin.readline

global m
n, m = map(int, input().split())
li = [0] * n
cnt = 0
total = 0

for i in range(len(li)):
    li[i] = (list(map(int, input().split())))

def crush(i, k):
    global cnt
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for g in range(1, m+1):
        for h in range(0, len(dx)):
            nx = i + dx[h] * g
            ny = k + dy[h] * g 
            tmp = 0
            try:
                tmp = li[nx][ny]
            except IndexError:
                pass

            if tmp == 2:
                return False

    return True

for i in range(len(li)):
    for k in range(len(li)):
        if li[i][k] == 1:
            total += 1
            if crush(i, k):
                cnt += 1
print(total - cnt)
