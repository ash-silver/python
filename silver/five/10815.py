import sys
input = sys.stdin.readline

n = int(input())
nList = set(input().split())
m = int(input())
mList = input().split()

nList.sort()

def binary(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else : end = mid -1
    return False

for i in range(0, len(mList)):
    if binary(mList[i], nList) == True:
        mList[i] = 1
    else:
        mList[i] = 0

print(*mList)

# import sys
# input = sys.stdin.readline

# n = int(input())
# nList = set(input().split())
# m = int(input())
# mList = input().split()

# res = ""
# for i in range(0, len(mList)):
#     if mList[i] in nList:
#         res += "1 "
#     else:
#         res += "0 "

# print(res)