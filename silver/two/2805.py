import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

start, end = 0, 1000000000

while start <= end:
    sum = 0
    mid = (end + start) // 2
    for i in li:
        if i > mid:
            sum += (i - mid)
        if sum > m:
            break
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
  


# def binary(start, end):
#     sum = 0
#     mid = int((end + start) / 2)
#     # tmp = li.index(mid)
#     for i in li:
#         if i > mid:
#             sum += (i - mid)

#     if sum == m:
#         return print(mid)
#     elif sum > m:
#         binary(mid + 1, end)
#     else :
#         binary(start, mid - 1)

# binary(start, end)
