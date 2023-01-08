import sys
input = sys.stdin.readline

b1, b2 = map(int, input().split())
day = int(input())
order = 1

for i in range(0, day):
    if order == 1:
        if b1%2 == 0:
            tmp = b1//2
        else:
            tmp = int(b1//2) + 1
        order = 2
        b1 -= tmp
        b2 += tmp

    else:
        if b2%2 == 0:
            tmp = b2//2
        else:
            tmp = int(b2//2) + 1
        order = 1
        b2 -= tmp
        b1 += tmp
print(b1, b2)