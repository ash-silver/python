import math
import sys

input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

def mode(n, num):
    cnt = list(range(1, n+1))
    cnt = [[] for k in range(0, n+1)]

    count = 1
    maximum = 1

    for k in range(1, n):
        if num[k] == num[k-1]:
            count += 1
        else: 
            cnt[count].append(num[k-1])
            maximum = max(count, maximum)
            count = 1
        if k == n-1:
            cnt[count].append(num[k])
            maximum = max(count, maximum)
    if n == 1:
        cnt[1].append(num[0])
    cnt[maximum].sort()
    if len(cnt[maximum]) == 1:
        return str(cnt[maximum][0])
    else:
        return str(cnt[maximum][1])

mean = round(sum(num)/n)
center = num[math.trunc(n/2)]

minus = num[n-1] - num[0]
print(mean)
print(center)
print(mode(n, num))
print(minus)

