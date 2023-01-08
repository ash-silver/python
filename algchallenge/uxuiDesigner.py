import sys
input = sys.stdin.readline

n, m = map(int, input().split())
event = [0 for i in range(0, n)]
for i in range(0, m):
    li = list(map(int, input().split()))
    for k in range(1, len(li)):
        event[li[k] - 1] += 1
maximum = max(event)
tmp = maximum
cnt = 1
while maximum == tmp:
    print(event.index(maximum) + cnt, end=" ")
    event.pop(event.index(max(event)))
    if len(event) == 0:
        break
    tmp = max(event)
    cnt += 1
    