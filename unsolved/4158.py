import sys
input = sys.stdin.readline

n, m = map(int, input().split())
di = dict()

for i in range(0, n):
    di[i] = int(input())
cnt = len(di)
for i in range(0, m):
    # try:
    di.popitem(int(input()))
    # except:
    #     cnt -= 1
input()
print(cnt)
