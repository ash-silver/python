import sys
input = sys.stdin.readline

# 크로아티아 알파벳
sen=list(input())
cnt = len(sen)- 1

for i in range(0, len(sen)):
    if sen[i] == '-':
        cnt -= 1
    elif sen[i] == 'j':
        if sen[i-1] == 'l' or sen[i - 1] =='n':
            cnt -= 1
    elif sen[i] == '=':
        cnt -= 1
        if sen[i - 1] == 'z' and sen[i - 2] == 'd':
            cnt -= 1
    else:
        continue
print(cnt)









# 피보나치 수 5

n = int(input())

def fibo(num):
    if num < 2:
        return num
    elif num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)

print(fibo(n))