import sys
input = sys.stdin.readline

def sol():
    pobi = list(map(int, input().split()))
    crong = list(map(int, input().split()))

    def maximum(li):
        answerLi = 0
        for i in li:
            hundred = i//100
            ten = i // 10 - hundred * 10
            one = i % 10
            tmpSum = hundred + ten + one
            tmpMul = hundred + ten + one
            tmpI = max(tmpSum, tmpMul)
            answerLi = max(tmpI, answerLi)
        return answerLi
    pobiAns = maximum(pobi)
    crongAns = maximum(crong)
    if pobiAns > crongAns:
        print(1)
    elif crongAns > pobiAns :
        print(2)
    elif crongAns == pobiAns:
        print(0)
    else:
        print(-1)
sol()