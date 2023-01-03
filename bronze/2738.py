import sys
input = sys.stdin.readline

n, m = map(int, input().split())
aLi, bLi = [0] * n, [0] * n

for i in range(0, n):
    aLi[i] = list(map(int, input().split()))
for i in range(0, n):
    bLi[i] = list(map(int, input().split()))

for i in range(0, n):
    for k in range(0, m):
        aLi[i][k] += bLi[i][k]

for i in range(0, n):
    for k in range(0, m):
        print(aLi[i][k], end = " ")
    print()