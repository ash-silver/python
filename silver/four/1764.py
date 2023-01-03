import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listen = set([input().rstrip() for i in range(0, n)])
watch = set([input().rstrip() for i in range(0, m)])

cntli = sorted(list(listen.intersection(watch)))

print(len(cntli))
for i in cntli:
    print(i)