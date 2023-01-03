import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
minecraft = [0] * n
answer1, answer2 = 987654321, -1

for i in range(0, n):
    minecraft[i] = map(int, input().split())

maximum = max(max(minecraft))
minimum = min(min(minecraft))

def isPossible(target):
    num = b
    for i in range(0, n):
        for k in range(0, m):
            if minecraft[i][k] == target:
                continue
            elif minecraft[i][k] > target:
                num += (minecraft[i][k] - target)
            else:
                num -= (target - minecraft[i][k])
    if num >= 0 : 
        return 1
    else:
        return 0

def time(target):
    result = 0
    for i in range(0, n):
        for k in range(0, m):
            if minecraft[i][k] == target:
                continue
            elif minecraft[i][k] > target:
                result += (minecraft[i][k] - target) * 2
            else:
                result += (target - minecraft[i][k])
    return result

for i in range(maximum, minimum - 1, -1):
    if isPossible(i):
        tmp = time(i)
        if tmp < answer1:
            answer1 = tmp
            answer2 = i
print(answer1, answer2)      

