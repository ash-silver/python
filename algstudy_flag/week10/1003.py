import sys
input = sys.stdin.readline

global fibo                                             #fibo 리스트를 global 변수로 선언                         
fibo = [[0 for _ in range(0, 2)] for _ in range(0, 41)] #fibo 리스트 : 모두 0으로 초기화 -> fibo[n][0]은 0이 호출되는 수, [1]은 1이 호출되는 수
fibo[0][0] = 1                                          #fibo 첫 번째에서 0이 선언 되는 수를 1로 초기화
fibo[0][1] = 0                                          #fibo 첫 번째에서 1이 선언 되는 수를 0으로 초기화
tmp = 1                                                 #fib 함수에서 반복되는 수를 줄이기 위해 tmp부터 실행하도록 tmp를 1로 정의


def fib(n):                                             #fib함수 정의
    global tmp                                          #tmp를 함수 내에서도 사용할 수 있도록 global 변수로~
    if fibo[n][0] == 0 and n > 0:                       #구하려는 피보나치 수가 0 -> 처음 구하는 수, 0이 아닐 때는 전에 이미 구했던 수.
        for k in range(tmp, n+1):                       #전에 구했던 tmp부터 구할 n까지 반복문으로 피보나치 수 구하기
            fibo[k][0] = fibo[k-1][1]                   #수하려는 수의 0호출 수 = 직전 피보나치 함수에서 1이 호출된 수
            fibo[k][1] = fibo[k-1][0] + fibo[k-1][1]    #구하려는 수의 1호출 수 = 직전 피보나치 수의 0과 1이 호출된 수의 합
            tmp = k + 1                                 #다음에는 k+1부터 반복문 돌리려고 tmp에 저장
    sen = str(fibo[n][0]) + " " + str(fibo[n][1])+"\n"  #sen에 출력해야 할 문자열 저장
    return sen                                          #해당 문자열을 리턴


t = int(input())                                        #테스트 케이스 수 입력 받기
n = [int(input()) for _ in range(t)]                    #테스트 케이스의 수만큼 n 입력 받아 리스트에 저장
result = ""                                             #result에 문자열 저장할거야!!
for i in range(len(n)):                                 #테스트 케이스의 수만큼 fib 함수 구해서 result에 이어붙이기
    result += fib(n[i])
print(result)


# def fib(n):
#     if n == 0:
#         global zero
#         zero += 1
#         return 0
#     elif n == 1:
#         global one
#         one += 1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# fibo = [[0]*2]*40

# for i in range(1, len(fibo)):
#     fibo[i][0] = fibo[i-1][1]
#     fibo[i][1] = fibo[i-1][0] + fibo[i-1][1]
# for k in range(len(fibo)):
#     print(str(fibo[k][0]) + " " + str(fibo[k][1]))

# for k in range(int(input())):
#     scan.append(int(input()))
# sen = ""
# for i in range(len(scan)):
#     zero, one = 0, 0
#     fib(scan[i])
#     sen += str(zero) + " " + str(one) + "\n"
# print(sen)