import sys
input = sys.stdin.readline

res = ""
li = [1] * 10
li[0] = [0]
li[1] = [1]
li[2] = [2, 4, 8]
li[3] = [3, 9, 7, 1]
li[4] = [4, 6]
li[5] = [5]
li[6] = [6]
li[7] = [7, 9, 3, 1]
li[8] = [8, 4, 2, 6]
li[9] = [9, 1]
for i in range(0, int(input())):
    a, b = map(int, input().split())
    a %= 10
    res += str(li[a % 10][b % len(li[a%10]) - 1]) + "\n"
print(res.rstrip())