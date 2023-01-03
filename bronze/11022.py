import sys
input = sys.stdin.readline

res = ""
for i in range(0, int(input())):
    a, b = map(int, input().split())
    res += "Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(a + b) + "\n"
print(res.rstrip())

