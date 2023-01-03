import sys
input = sys.stdin.readline

a, b = map(int, input().split())
res = ""
while a != 0 and b != 0:
    if b % a == 0:
        res += "factor\n"
    elif a % b == 0:
        res += "multiple\n"
    else: 
        res += "neither\n"
    a, b = map(int, input().split())

print(res)
        

