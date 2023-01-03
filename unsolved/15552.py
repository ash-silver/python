import sys
input = sys.stdin.readline

t = int(input())
res = ""

for i in range(0, t):
    a, b = map(int, input().split())
    res += str(a + b) + "\n"
print(res.rstrip())