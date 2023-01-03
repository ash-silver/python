import sys
input = sys.stdin.readline

n = int(input())

for k in range(n, 0, -1):
    for i in range(0, n - k):
        print(" ", end ="")
    for i in range(1, (k)*2):
        print("*", end = "")
    if k != 0:
        print()

for k in range(1, n):
    for i in range(0, n - k - 1):
        print(" ", end ="")
    for i in range(1, (k+1)*2):
        print("*", end = "")
    print()