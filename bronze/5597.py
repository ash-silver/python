import sys
input = sys.stdin.readline
li = [i for i in range(1, 31)]

for i in range(0, 28):
    num = int(input())
    if num in li:
        li.pop(li.index(num))

for i in li:
    print(i)