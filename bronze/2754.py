import sys
input = sys.stdin.readline

score = input()
result = 0.0

if score[0] == 'A':
    result = 4.0
elif score[0] == 'B':
    result = 3.0
elif score[0] == 'C':
    result = 2.0
elif score[0] == 'D':
    result = 1.0
else :
    result = 0.0

if score[1] == '+':
    result += 0.3
elif score[1] == '-':
    result -= 0.3

print(result)
