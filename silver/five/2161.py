import sys
input = sys.stdin.readline

li = [i for i in range(1, int(input()) + 1)]
cnt = 0
res = list()

while len(li) > 1:
    if cnt == 0:
        res.append(li.pop(0))
        cnt += 1
    else:
        li.append(li.pop(0))
        cnt -= 1
res.append(li.pop())
for i in res:
    print(i, end=" ")