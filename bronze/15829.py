from re import L
import sys
input = sys.stdin.readline

r = 31
m = 1234567891

n = int(input())
l = input().rstrip()
sum = 0


for i in range(0, len(l)):
    tmp = ((ord(l[i]) - 96)) * ((31 ** (i)) % m)
    sum += (tmp % m)
print(sum % m)