import sys
input = sys.stdin.readline

n = input().rstrip()

li = [int(n[i]) for i in range(0, len(n))]
cnt = 0

while sum(li) >= 10:
    li = str(sum(li))
    li = [int(li[i]) for i in range(0, len(li))]
    cnt += 1

if len(n) == 1:
    if int(n) % 3 == 0:
        print("0\nYES")
    else:
        print("0\nNO")
elif sum(li) % 3 == 0:
    print(str(cnt + 1) + "\n" + "YES")
else:
    print(str(cnt + 1) + "\n" + "NO")