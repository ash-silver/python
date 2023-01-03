import sys
input = sys.stdin.readline

a, b = 1, 0

for i in range(0, int(input())):
    tmp = a
    a = b
    b += tmp

print(str(a) + " " + str(b))