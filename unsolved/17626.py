import math
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while n >= 1:
    n -= int(math.sqrt(n)) * int(math.sqrt(n))
    cnt += 1
print(cnt)