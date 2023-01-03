import sys
input = sys.stdin.readline

cnt = 0
day = int(input())
li = list(map(int, input().split()))

for i in li:
    if day == i:
        cnt += 1
print(cnt)