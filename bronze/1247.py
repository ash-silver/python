import sys
input = sys.stdin.readline

res = ""

for i in range(0, 3):
    sum = 0
    for k in range(0, int(input())):
        sum += int(input())
        
    if sum == 0 :
        res += "0\n"
    elif sum > 0:
        res += "+\n"
    elif sum < 0: 
        res += "-\n"
print(res)