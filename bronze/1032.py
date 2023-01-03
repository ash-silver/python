import sys
input = sys.stdin.readline

n = int(input())
li = [input().rstrip() for i in range(0, n)]
res = [li[0][i] for i in range(0, len(li[0]))]

for i in range(1, len(li)):
    for k in range(0, len(li[0])):
        if li[i][k] != li[0][k]:
            res[k] = "?"
for i in res:
    print(i, end="")