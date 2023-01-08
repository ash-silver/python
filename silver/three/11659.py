import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
sumLi = [0]
for i in range(0, len(li)):
    sumLi.append(li[i] + sumLi[i])
answer = ""

for k in range(0, m):
    i, j = map(int, input().split())
    answer += str(sumLi[j] - sumLi[i - 1]) + "\n"
print(answer.rstrip())