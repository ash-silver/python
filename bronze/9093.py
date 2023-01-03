import sys
input = sys.stdin.readline

t = int(input())
li = [""] * t
sen = ""
for i in range(0, t):
    li[i] = list(input().split())

    for k in range(0, len(li[i])):
        for g in range(len(li[i][k]) - 1, -1, -1):
            sen += str(li[i][k][g])
        sen += " "
    sen += "\n"
print(sen)