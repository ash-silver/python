import sys
input = sys.stdin.readline

n = input().rstrip()
res = 0

if len(n) == 1:
    res = int(n)
else:
    for i in range(0, len(n) - 1):
        res += ((10 ** i) * 9) * (i + 1)
    res += (int(n) - ((10 ** (i + 1)) - 1)) * len(n)
print(res)

# for i in range(1, len(n)):
#     res += (10 ** (i - 1)) * 9
# tmp = n[1:]
# try:
#     res += ((int(tmp)+ 1) * len(n))
# except ValueError:
#     res = int(n)
