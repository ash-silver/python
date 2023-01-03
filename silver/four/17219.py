import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pwDict  = dict()
result = ""

for i in range(0, n):
    key, val = input().split()
    pwDict[key] = val

for i in range(0, m):
    req = input().rstrip()
    result += str(pwDict.get(req))

print(result)