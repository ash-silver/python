import sys
input = sys.stdin.readline

# a = 고정 비용, b = 한 대 생산 비용, c = 노트북 가격
a, b, c = map(int, input().split())

if (c - b) <= 0:
    print(-1)
else:
    print(int(a/(c-b)) + 1)