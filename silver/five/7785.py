import sys
input = sys.stdin.readline

log = dict()

for i in range(0, int(input())):
    name, exist = input().split()
    if exist == "enter":
        log[name] = exist
    else :
        log.pop(name)

res = list(log.keys())
res.sort(reverse=True)

for i in res:
    print(i)