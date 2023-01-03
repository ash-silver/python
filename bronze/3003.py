import sys
input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))

for i in range(0, len(chess)):
    chess[i] -= li[i]
print(*chess, sep =" ")