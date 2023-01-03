import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n
for i in range(0, n):
    li[i] = list(map(int, input().split(' ')))

for i in range(1, n):
    li[i][0] += li[i - 1][0]
    li[i][len(li[i]) - 1] += li[i - 1][len(li[i - 1]) - 1]
    for k in range(1, len(li[i]) - 1):
        li[i][k] += max(li[i - 1][k - 1], li[i - 1][k])
print(max(li[n - 1]))