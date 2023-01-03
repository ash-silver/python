import sys
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
s.sort()
n = int(input())
cnt = 0

minimum, maximum = 1, s[len(s) - 1]
for i in s:
    if i == n:
        maximum, minimum = i, i
        break
    elif i < n:
        minimum = i + 1
    elif i > n:
        maximum = i
        break

li = [i for i in range(minimum, maximum)]

for i in range(0, len(li)):
    if li[0] < n:
        cnt += (len(li) - li.index(n))
    elif li[0] > n :
        cnt += len(li)
    elif li[0] == n :
        cnt += len(li) - 1
    if li[0] >= n:
        break
    li.remove(li[0])

print(cnt)
