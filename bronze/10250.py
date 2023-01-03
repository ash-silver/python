import sys
input = sys.stdin.readline

res = []
for i in range(0, int(input())):
    h, w, n = map(int, input().split())
    
    # 꼭대기 층
    if n % h == 0:
        res.append((h * 100 ) + (n // h))
    else:
        res.append(((n % h) * 100 ) + (n // h + 1))

for i in range(0, len(res)):
    print(res[i])
