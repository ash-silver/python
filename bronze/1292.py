import sys
input = sys.stdin.readline

a, b = map(int, input().split())
sum = 0
li = []

for i in range(1, b + 1):
    for k in range(0, i):
        li.append(i)
for i in range(a - 1, b):
    sum += li[i]
print(sum)
 
