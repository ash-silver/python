import sys
input = sys.stdin.readline

sen = ""
for i in range(0, int(input())):
    a, b = map(int, input().split(","))
    sen += str(a + b) + "\n"
print(sen.rstrip())
