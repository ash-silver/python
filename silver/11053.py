import sys
input = sys.stdin.readline

listLen = int(input())
li = list(map(int, input().split()))

cnt = 1


def cnt(start):
    tmp = start
    for i in range(start + 1, len(li)):
        if li[tmp] < li[i]:
            cnt += 1
            tmp = i
            
