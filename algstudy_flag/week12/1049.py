import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 첫 번째 브랜드의 패키지와 낱개 가격 입력 받기
sixPrice, onePrice = map(int, input().split())

# 두 번쨰 브랜드부터 패키지와 낱개 가격 입력 받기
for i in range(1, m):
    tmp1, tmp2 = map(int, input().split())
    # 그 전 브랜드의 최소값과 방금 입력 받은 브랜드의 값 중 최소값을 sixPrice와 onePrice에 저장
    sixPrice, onePrice = min(sixPrice, tmp1), min(onePrice, tmp2)
    
# 패키지 가격이 낱개 가격 6개 보다 쌀 경우
if sixPrice <= onePrice * 6:
    # 1) 패키지로 살 수 있는 만큼 사고 낱개로 나머지 사는 것
    # vs
    # 2) 1)보다 패키지 하나를 더 사는 게 더 쌀 경우
    # 1)과 2) 중에 최소값을 프린트 
    print(min((sixPrice * (n // 6) + onePrice * (n % 6)), (sixPrice * (n//6 + 1))))
# 패키지 가격이 낱개 가격 * 6보다 비싸서 낱개로만 사는 것이 쌀 경우
else:
    print(onePrice * n)