import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

primeList = []

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for k in range(m, n + 1):
    if k == 1:
        continue
    elif isPrime(k) == True:
        primeList.append(k)
        
if len(primeList) == 0:
    print(-1)
else:
    print(sum(primeList))
    print(min(primeList))
