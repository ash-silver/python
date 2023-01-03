import sys
input = sys.stdin.readline

n = int(input())
li = list()
li = list(map(int, input().split()))
v = int(input()) 

cnt = 0

for i in li:
    if i == v:
        cnt += 1
print(cnt)