import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())
result = ""
for i in range(0, n, 2):
    tmp = ord(s[i]) + (int(s[i + 1]) ** 2)
    while tmp > 122:
        tmp -= 26
    result += chr(tmp)
print(result)