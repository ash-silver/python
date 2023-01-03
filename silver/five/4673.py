import sys
input = sys.stdin.readline


def constructor(index):
    global num
    sum = 0
    tmp = origin[index]
    sum += tmp
    while tmp > 0:
        sum += tmp % 10
        tmp = tmp // 10
    if sum in num:
        num.remove(sum)


origin = list(set(range(1, 10001)))
num =  list(set(range(1, 10001)))

for k in range(0, len(num)):
    try :
        constructor(k)
    except IndexError:
        break
for g in range(0, len(num)):
    print(num[g])