import sys
input = sys.stdin.readline

n = input()
li = []
for i in range(0, len(n)):
    li.append(n[i])
li.sort(reverse=True)
for i in range(0, len(n)-1):
    print(li[i], end="")