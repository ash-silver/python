import sys
input = sys.stdin.readline

question = []

for i in range(0, int(input())):
    question.append(int(input()))

padovan = [0] * (max(question) + 1)

padovan[1], padovan[2], padovan[3] = 1, 1, 1
padovan[4], padovan[5] = 2, 2
padovan[6], padovan[7], padovan[8] = 3, 4, 5
padovan[9] = 7
padovan[10] = 9

for i in range(11, max(question) + 1):
    padovan[i] = padovan[i - 1] + padovan[i - 5]

for i in question:
    print(padovan[i])