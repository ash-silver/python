import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0] * n
cnt = 0
for i in range(0, n):
    graph[i] = list(input().rstrip())
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
