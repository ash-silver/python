import math
import sys
input = sys.stdin.readline
fact = math.factorial

li = []


# 테스트 케이스 수 입력 
for testcase in range(0, int(input())):
    num = int(input())
    sum = 0
    # 3이 들어가는 숫자를 0부터 
    for cnt3 in range(0, int(num/3) + 1):
        # 2가 들어가는 숫자를 0부터
        for cnt2 in range(0, int((num - (cnt3 * 3))/2) + 1):
            # 1이 들어가는 숫자 = (num - 3의 개수 - 2의 개수)
            cnt1 = (num - cnt3 * 3 - cnt2 * 2)
            # 같은 것이 있는 순열 공식 = n!/(3의 개수)! * (2의 개수)! * (1의 개수)!
            sum += (fact(cnt3 + cnt2 + cnt1)/(fact(cnt3) * fact(cnt2) * fact(cnt1)))
    # 나중에 출력하려고 list에 입력
    li.append(math.trunc(sum))
for i in li:
    print(i)
            