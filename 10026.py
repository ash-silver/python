from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

blindness, noraml = 0, 0
dx = [1, 0]
dy = [0, 1]

map = [''] * n
for i in range(0, n):
    map[i] = list(input().rstrip())

visited = [False] * (len(map[0]) * n)

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if (x >= (len(map[0]) - 1)) and (y >= (n - 1)):
            return
        for i in range(0, 2):
            nx = x + dx[i]
            ny = y + dy[i]
        
        