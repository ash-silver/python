import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n
count = 1

# list 입력
for i in range(0, n):
    li[i] = list(map(int, input().split()))

li.sort(key=lambda x : (x[1], x[0]))

last = li[0][1]

for i in range(1, len(li)):
    if li[i][0] >= last:
        count += 1
        last = li[i][1]
print(count)