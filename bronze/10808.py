import sys
input = sys.stdin.readline

li = [0] * 26
sen = input().rstrip()
for i in range(0, len(sen)):
    tmp = ord(sen[i])
    li[tmp - 97] += 1
print(*li, sep = " ")
