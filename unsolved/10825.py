import sys
input = sys.stdin.readline

n = int(input())
li = [0]*n
for i in range(0, n):
    li[i] = list(input().split())
    li[i][1], li[i][2], li[i][3] = int(li[i][1]), int(li[i][2]), int(li[i][3])

li.sort(key=lambda li:li[1])

    


print(*li)