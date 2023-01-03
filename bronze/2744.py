import sys
input = sys.stdin.readline

sen = list(input().rstrip())
for i in range(0, len(sen)):
    if ord(sen[i]) < 97:
        sen[i] = chr(ord(sen[i]) + 32)
    else:
        sen[i] = chr(ord(sen[i]) - 32)
for i in sen:
    print(i, end="")