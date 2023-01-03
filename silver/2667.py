from collections import deque
import sys
input = sys.stdin.readline

cnt = 0
# 지도의 크기 입력
n = int(input())

# 지도 입력
map = [0] * n
for i in range(0, n):
    map[i] = input().rstrip()

# 방문 여부 리스트
visited = [[False for i in range(0, n)] * n]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, visited):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    map[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(n) or nx < 0 or ny >= len(n) or ny < 0:
                continue
            if map[x][y] == 1:
                cnt += 1
                map[x][y] = 0

       