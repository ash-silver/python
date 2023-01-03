import sys
input = sys.stdin.readline

n = int(input())
maximum = 0
rope = [0] * n

for i in range(0, n):

    rope[i] = int(input())

rope.sort()

for i in range(0, n):
    maximum = max(maximum, (rope[0] * (n - i)))
    rope.pop(0)

print(maximum)