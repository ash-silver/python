import sys
input = sys.stdin.readline

# tmp = 해당 칸에서의 사람
# max = 지금까지의 max값

tmp, maximum = 0, 0

for i in range(0, 4):
    a, b = map(int, input().split())
    tmp -= a
    tmp += b
    maximum = max(maximum, tmp)

print(maximum)