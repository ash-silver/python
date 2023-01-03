import sys
input = sys.stdin.readline

n = int(input())
cnt, tmp = 0, n

while tmp != n or cnt == 0:
    tmp = (tmp//10 + tmp%10)%10 + tmp%10*10
    cnt += 1

print(cnt)