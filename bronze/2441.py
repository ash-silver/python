import sys
input = sys.stdin.readline

n = int(input())
for k in range(n, 0, -1):

    for i in range(0, n - k): 
        print(" ", end ="")
    for i in range(0, k):
        print("*", end ="")
    print()