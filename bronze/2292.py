import sys
input = sys.stdin.readline

n = int(input())
i = 1
res = 0

if n == 1:
    res = 1
elif n <= 7:
    res = 2
else:
    n -= 7
    while n > 0:
        n -= (6 + i * 6)
        res = (i + 2)
        i += 1

print(res)