import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

li = [] * (n + 1)

for i in range(0, m):
    tmp1, tmp2 = map(int, input().split())
    li[tmp1].append(tmp2)

def goorm(num):
    