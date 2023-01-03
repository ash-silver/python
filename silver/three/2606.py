from collections import deque
import sys
input = sys.stdin.readline

# 컴퓨터 수
n = int(input())
# 연결된 컴퓨터 쌍
connect = int(input())

# '컴퓨터 수'만큼 리스트 크기 선언
li = [[] for i in range(0, n + 1)]
cnt = 0

for i in range(0, connect):
    tmp1, tmp2 = map(int, input().split())
    li[tmp1].append(tmp2)
    # 양방향 추가
    li[tmp2].append(tmp1)

# 방문 확인 리스트 초기화
visited = [False for i in range(0, len(li))]


def bfs(x, visited):
    # bfs 함수에서 cnt를 global로 정의하지 않으면 접근 불가능
    global cnt
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        x = queue.popleft()
        for i in range(0, len(li[x])):
            if visited[li[x][i]] == True:
                continue
            visited[li[x][i]] = True
            cnt += 1
            queue.append(li[x][i])
            bfs(li[x][i], visited)
            
# 1번 컴퓨터가 바이러스 걸렸을 때! 
bfs(1, visited) 
print(cnt)
