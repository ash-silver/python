import sys
input = sys.stdin.readline

n, m = map(int, input().split())
aLi = []
for i in range(0, n):
    aLi.append(list(map(int, input().split())))

m, k = map(int, input().split())
bLi = []
for i in range(0, m):
    bLi.append(list(map(int, input().split())))

tmp = 0 
# for i in range(0, n):
#     for k in range(0, m):
        