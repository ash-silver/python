import sys
input = sys.stdin.readline

li = [0] * int(input())

for i in range(0, len(li)):
    li[i] = list(map(int, input().split()))
    for k in range(0, 2):
        li[i].pop(li[i].index(max(li[i])))

for i in range(0, len(li)):
    print(max(li[i]))