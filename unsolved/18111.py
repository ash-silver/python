import sys
input = sys.stdin.readline

global gDo

n, m, b = map(int, input().split())
tmp = b
gDo = [0] * n
maximum , minimum = 0, 256
li = [(500 * 500 * 256)] * 256

for i in range(0, n):
    gDo[i] = list(map(int, input().split()))

# maximum = max(max(gDo))
# minimum = min(min(gDo))

def time(height):
    global b
    sum = 0 
    for k in range(0, len(gDo)):
        if sum >= min(li):
            return (500 * 500 * 256)
        for g in range(0, len(gDo[k])):
            if gDo[k][g] > height:
                sum += (2 * gDo[k][g] - height)
            elif gDo[k][g] < height:
                if b < 1:
                    return (500 * 500 * 256)
                sum += height - gDo[k][g]
                b -= 1
    return sum
        
for i in range(0, 256 + 1):
    b = tmp
    li[i] = time(i)
for i in range(0, 256 - 1, -1):
    if li[i] == min(li):
        print(str(min(li)) + " " + str(i))
        break