import sys
import math
input = sys.stdin.readline

sen = ""

for i in range(int(input())):
    n, m = map(int, input().split())
    sen += str(math.comb(max(n, m), min(n, m))) + "\n"

print(sen)