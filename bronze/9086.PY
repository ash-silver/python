import sys
input = sys.stdin.readline

result = []
for i in range(0, int(input())):
    sen = input().rstrip()
    tmp = sen[0] + sen[len(sen) - 1]
    result.append(tmp)

for i in result:
    print(i)