import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

li = [list() for k in range(0, n + 1)]

for i in range(0, m):
    a, b = map(int, input().split())
    # (a,b)가 li에 있는지 확인
    if a not in li:
        # li[a] = b
        li[a].append(b)
    elif b not in li[a]:
        # li[b] = a
        li[b].append(a)
    # (b,a)가 li에 있는지 확인 (양방향으로 넣어줘야함.)      
    if b not in li:
        # li[b] = a
        li[b].append(a)
    elif a not in li[b]:
        # li[a] = b
        li[a].append(b)
    
global visitedDfs
visitedDfs = [] 

def dfs(list, start):
    stack = [start]
    while stack:
        t = stack.pop()
        if t not in visitedDfs:
            visitedDfs.append(t)
            if list[t]:
                for g in list[t]:
                    dfs(list, g)

dfs(li, v)
print(visitedDfs)

global visitedBfs
visitedBfs = [] 

def bfs(list, start):
    queue = [start]
    while queue:
        t = queue.pop()
        if t not in visitedBfs:
            visitedBfs.append(t)
            for g in list[t]:
                if g not in visitedBfs:
                    visitedBfs.append(g)
                    queue.append(g)
bfs(li, v)
print(visitedBfs)        