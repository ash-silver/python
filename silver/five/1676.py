from math import factorial
import sys
input = sys.stdin.readline

li = list(str(factorial(int(input()))))
cnt = 0

for i in range(len(li) - 1, 0, -1):
    if li[i] != '0':
        break
    elif li[i] == '0':
        cnt += 1
print(cnt)
    