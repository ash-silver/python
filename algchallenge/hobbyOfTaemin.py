import sys
input = sys.stdin.readline
n = int(input())
sum = (((n * (n + 1)))//2) ** 2
print(int(sum % 1000000007))