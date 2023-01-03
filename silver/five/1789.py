import sys
input = sys.stdin.readline

s = int(input())
cnt = 0
x = 1

while 1:
    s -= x
    cnt += 1
    if s < 0:
        break
    x += 1
print(cnt - 1)


