import sys
input = sys.stdin.readline

cnt = 14
bingo = [[0] * 5] * 5
find = [] * 25
isBingo = [0, 0, 0, 0, 0]
 
for i in range(0, 5):
    bingo[i] = list(map(int, input().split()))
for i in range(0, 5):
    find = map(int, input().split())

    




# for i in range(0, 5):
#     for k in range(0, 5):
#         print(bingo[i][k], end = " ")
#     print()