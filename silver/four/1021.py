import sys
input = sys.stdin.readline

n, m = map(int, input().split())
origin = list(range(1, n+1))
want = list(map(int, input().split()))

tmp = origin.index(want[0])
cnt = min(tmp, len(origin)-tmp)

for i in range(1, m):
    origin.pop(tmp)
    cnt += min(abs(origin.index(want[i]) - tmp), abs(len(origin) - abs(origin.index(want[i]) - tmp)))
    tmp = origin.index(want[i])

print(cnt)
    # front = abs(origin.index(want[i]) - tmp)
    # back = abs(len(origin) - front)
