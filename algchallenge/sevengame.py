import sys
input = sys.stdin.readline

ans = 0
result = list()
scan = list()
for i in range(0, 5):
    scan.append(list(input().rstrip()))
for i in range(0, 5):
    num = list(scan[i])
    ans = int(num[0]) + int(num[2]) + int(num[4]) + int(num[6])
    for k in range(1, 6, 2):
        if int(num[k]) != 0:
            ans *= int(num[k])
    result.append(int(ans%10))
for i in result:
    print(i)