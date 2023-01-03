import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for i in range(0, n)]
isVisited = [0 for i in range(0, n)]
i, score = 0, 0

while 1:
    # a = li[i] + li[i + 1] + li[i + 2]
    # b = li[i] + li[i + 1] + li[i + 3]
    # c = li[i] + li[i + 2]  
    a = li[i + 1] + li[i + 2]
    b = li[i + 1] + li[i + 3]
    c = li[i + 2]
    big = max(max(a, b), c)
    score += big
    # isVisited[i] = 1

    # 1, 1, 1
    if big == a:
        # isVisited[i + 1], isVisited[i + 2], isVisited[i + 3] = 1, 1, 0
        i += 4

    # 1, 1, 0 
    elif big == b:
        # isVisited[i + 1], isVisited[i + 2] = 1, 0
        i += 3
        
    # 1, 0, 1
    else:
        # isVisited[i + 1], isVisited[i + 2] = 0, 1
        i += 2

    if i == (n - 3):
        score += max((li[i] + li[i + 1]), (li[i] + li[i + 2]))
        break
    elif i == (n - 4):
        score += (li[i + 2] + li[i + 3])
        break
    
print(score + li[len(li) - 1])       

