from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [''] * n
cnt = n * m

for i in range(0, len(map)):
    map[i] = list(input().rstrip())
    
visited = [[False] * len(map[0])] * len(map)
tmp = map[0][0]
dx = [1, 0]
dy = [0, 1]


def bfs(i, k):

    global cnt

    for k in range(0, n):
        for i in range(0, m):

            if i >= (m - 1) and k >= (n - 1):
                return
            
            if visited[k][i] == True:
                continue
            try:
                if map[k][i] == '-':
                    if map[k + 1][i] == '-':
                        visited[k + 1][i] == True
                        cnt -= 1
                        continue
                    else:
                        continue  
            except IndexError:
                pass

            try:
                if map[k][i] == '|':
                    if map[k][i + 1] == '|':
                        visited[k][i + 1] == True
                        cnt -= 1
                        continue
                    else:
                        continue
            except IndexError:
                pass   
bfs(0, 0)
print(cnt)         



    


