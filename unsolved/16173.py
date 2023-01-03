from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

# jelly 지도 만들기
jelly = []
for i in range(0, n):
    jelly.append(list(map(int, input().split())))

# 방문 여부 확인
visited = []
for i in range(0, n):
    visited.append([False] * n)

# 움직이기 dx -> (x좌표 + 1), dy -> (y좌표 + 1)
dx = [1, 0]
dy = [0, 1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))

    # 방문 표시
    visited[x][y] = True

    # 모두 방문할 때까지 while문 돌리기
    while queue:
        # (x, y)를 방문 했으니 없애기
        x, y = queue.popleft()

        # 마지막 지점에 방문했으면 '하루하루' 리턴 후 종료
        if jelly[x][y] == -1:
            return 'HaruHaru'
        
        # x쪽으로 한 번, y쪽으로 한 번 가기
        for i in range(0, 2):

            # x, y 좌표에 있는 값 만큼 이동해 nx, ny에 저장
            nx = x + dx[i] * jelly[x][y]
            ny = y + dy[i] * jelly[x][y]

            # 범위를 벗어나는 경우, 다음 경우 시행
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 이미 방문한 경우, 다음 경우 시행
            if visited[nx][ny] == True:
                continue

            # 위 두 경우가 아닌 경우, 이동
            if visited[nx][ny] == False:
                visited[nx][ny] == True
                queue.append((nx, ny))

    return 'Hing'

print(bfs(0, 0, visited))

# a, b = 0, 0
# global location
# global visited
# location = jelly[a][b]

# def right(num):
#     global a
#     global b
#     b += num

#     try:
#         visited[a][b] = True
#     except IndexError:
#         return False
#     location = jelly[a][b]
#     if a == n-1 and b == n-1:
#         return True
#     else:
#         explore(location)



# def under(num):
#     global a
#     global b
#     a += num
#     try:
#         visited[a][b] = True
#     except IndexError:
#         return False
#     location = jelly[a][b]
#     if a == n-1 and b == n-1:
#         return True
#     else:
#         explore(location)



# def explore(num):
#     global a
#     global b
#     # tmpA, tmpB = a, b
#     if right(num) == True:
#         return True
#     # a, b = tmpA, tmpB
#     a, b, num = 0, 0, jelly[0][0]
    
#     if under(num) == True:
#         return True
#     else:
#         return False


# if explore(location) == False:
#     print("Hing")
# else:
#     print("HaruHaru")


# def dfs(jelly, v, visited):
#     visited[v] = True
#     print(v, end='')
#     for i in jelly[v]:
        
#         if not visited[v]:              #방문하지 않았다면
#             dfs(jelly, v, visited)

