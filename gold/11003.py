import sys
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
d = ""

for i in range(0, n):
    tmp = i - l + 1
    if tmp > i:
        d += str(min(a[i:tmp + 1])) + " "
    elif tmp > 0:
        d += str(min(a[tmp:i + 1])) + " "
    else:
        d += str(min(a[0:i + 1])) + " "
print(d)