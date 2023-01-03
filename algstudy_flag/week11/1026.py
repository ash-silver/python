import sys
input = sys.stdin.readline

n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_a.sort()

s = 0
for g in range(len(list_a)):
    s += list_a[g] * max(list_b)
    list_b.remove(max(list_b))

print(s)

# 어떻게 해야 s가 작을까,,,,
#  a = 123
#  b = 123
#  1*1 + 2*2 + 3*3 = 14
#  1*3 + 2*2 + 3*1 = 10