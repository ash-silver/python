import sys
input = sys.stdin.readline

n = list(input().rstrip())

def cal(n):
    num = [0]*10
    for i in range(0, len(n)):
        if int(n[i]) == 6:
            if num[9] < num[6]:
                num[9] += 1
            else:
                num[6] += 1
        elif int(n[i]) == 9:
            if num[6] < num[9]:
                num[6] += 1
            else:
                num[9] += 1
        else:
            num[int(n[i])] += 1
    return max(num)
print(cal(n))
