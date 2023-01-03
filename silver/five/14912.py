import sys
input = sys.stdin.readline

n, d = map(int, input().split())
sen = ""
cnt = 0

for i in range(1, n + 1):
    sen += str(i)
for i in range(0, len(sen)):
    if int(sen[i]) == d:
        cnt += 1

print(cnt)

