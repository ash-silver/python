import sys
input = sys.stdin.readline


fibo = [i for i in range(0, int(input()) + 1)]
for i in range(2, len(fibo)):
    fibo[i] = fibo[i - 1] + fibo[i-2]
print(fibo[len(fibo) - 1])

