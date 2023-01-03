import sys
input = sys.stdin.readline

case = []
for i in range(0, int(input())):
    case.append(sum(map(int, input().split())))
for i in range(0, len(case)):
    print("Case #" + str(i + 1) + ": " + str(case[i]))