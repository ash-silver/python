import sys
input = sys.stdin.readline

global cnt, rank
n, score, cnt  = map(int, input().split())

rank = 1

def rankPrint():
    if cnt >= rank:
        return rank
    else:
        return -1

if n == 0 :
    print(rankPrint())
else:
    li = list(map(int, input().split()))
    for i in range(0, len(li)):
        if li[i] < score:
            print(rankPrint())
            break
        elif li[i] < score:
            if cnt == rank:
                print(-1)
                break
            elif cnt > rank:
                print(rankPrint())

        elif li[i] == score:
            if cnt == rank:
                print(-1)
                break
            else:
                print(rankPrint())
                break
        elif i == len(li) - 1 and cnt > rank:
            print(rank + 1)
            break
        else :
            rank += 1
            continue

