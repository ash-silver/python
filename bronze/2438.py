import sys
input = sys.stdin.readline

n = int(input())

for i in range(0, n):
    for k in range(0, i + 1):
        print("*", end ="")
    print()    

