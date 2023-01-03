import sys
input = sys.stdin.readline

li = [int(input()) for i in range(0,3)]
bev = [int(input()) for i in range(0,2)]
print(min(li) + min(bev) - 50)