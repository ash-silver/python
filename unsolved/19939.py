from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ball = [i for i in range(1, n + 1)]

list(combinations(ball, k))
