import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
sixNum = 0
li = [0 for i in range(0, 10)]

for i in range(0, len(n)):
    if n[i] == 9:
        n[i] = 6
    li[n[i]] += 1
if li.index(max(li)) == 6:
    tmp = li[6] % 2
    li[6] = li[6] // 2 + tmp
print(max(li))

