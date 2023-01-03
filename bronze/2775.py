import sys
input = sys.stdin.readline

t = int(input())
res = []
house = [[0 for i in range(0, 14)] for k in range(0, 15)]

for i in range(0, 14):
    house[0][i] = i + 1


for i in range(1, len(house)):
    for k in range(0, len(house[i])):
        for g in range(0, k + 1):
            house[i][k] += house[i - 1][g]

for i in range(0, t):
    n = int(input())
    k = int(input())
    res.append(house[n][k - 1])

for i in res:
    print(i)
