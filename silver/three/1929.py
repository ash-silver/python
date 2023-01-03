import sys
input = sys.stdin.readline

m, n = map(int, input().split())
# 구한 소수 집어 넣을 리스트 선언
primeNum = []

def isPrime(x):
    # 1일 경우를 예외 처리
    if x <= 1:
        return False
    # 2일 경우부터 소수인지 판별
    for i in range(2, int((x ** (1/2)) + 1)):
        if x % (i) == 0:
            # 나누어 떨어지는 경우 = 소수
            return False
    # 소수로 판별나지 않고 for문을 빠져나온 경우 != 소수
    return True

# m이상 n이하의 모든 숫자를 isPrime 함수를 확인
for i in range(m, n + 1):
    if isPrime(i):
        primeNum.append(i)

for i in primeNum:
    print(i)        