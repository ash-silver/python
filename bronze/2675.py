import sys
input = sys.stdin.readline

res = []

for i in range(0, int(input())):
    r, s = input().split()
    tmp = ""
    for k in s:
        tmp += str(k) * int(r)
    res.append(tmp)

for i in res:
    print(i)
