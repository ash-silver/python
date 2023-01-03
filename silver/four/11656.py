import sys
input = sys.stdin.readline

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

sen = list(input())
li = []

for i in range(0, len(sen) -1):
    li.append(convert(sen))
    sen.pop(0)
li.sort()

print(*li, sep="")