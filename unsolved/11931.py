import sys
input = sys.stdin.readline

n = int(input())
li = list()
for i in range(0, n):
    li.append(int(input()))
li.sort(reverse=True)
for i in range(0, n):
    print(li[i])