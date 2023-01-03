import sys
input = sys.stdin.readline
li = []

scan = input()

while scan !="\n":
    li.append(scan)
    scan = input()
print(*li)