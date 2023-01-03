import sys
input = sys.stdin.readline

res = ""
n, m = input().split()

li = dict()
for i in range(0, int(n)):
    li[i] = input().rstrip()
for i in range(0, int(m)):
    find = input()
    try:
        res += str(dict.values())
    except ValueError:
        res += str(dict.items(find) + 1) + "\n"
print(res.rstrip())