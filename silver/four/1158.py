import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# queue = [num for num in range(1, n + 1)]
queue = list(range(1, n+1))
res = "<"
i = 0
while len(queue) > 1:
    i = (i + k - 1) % len(queue)
    res += str(queue.pop(i)) + ", "
res += str(queue.pop()) + ">"
print(res) 