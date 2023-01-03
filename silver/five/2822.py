import sys
input = sys.stdin.readline

li = [int(input()) for i in range(0, 8)]
cp = li.copy()

sum = 0
answerLi = [0] * 5

for i in range(0, 5):
    sum += max(li)
    answerLi[i] = int(cp.index(max(li))) + 1
    li.remove(max(li))

answerLi.sort()

print(sum)
for i in range(0, len(answerLi)):
    print(answerLi[i], end =" ")