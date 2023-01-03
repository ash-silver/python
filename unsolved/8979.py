import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = [0] * n
for i in range(0, n):
    li[i] = list(map(int, input().split()))

li.sort(key = lambda x : (-x[1], -x[1], -x[2]))
