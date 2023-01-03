import sys
input = sys.stdin.readline


def yesOrNo(sentence):
    tmp = []
    for i in range(0, len(sentence)):
        if sentence[i] == '(':
            tmp.append('(')
        else:
            if len(tmp) < 1:
                return "NO"
            else:
                tmp.pop()
    if len(tmp) == 0:
        return "YES"
    else:
        return "NO"


n = int(input())
li = [0] * n
for i in range(0, n):
    li[i] = yesOrNo(input().rstrip())

for i in li:
    print(i)