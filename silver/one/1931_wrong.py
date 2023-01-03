import sys
input = sys.stdin.readline

def popList(indexNum):
    global li
    for k in range(indexNum, len(li) - 1):
        li[k][0], li[k][1] = li[k + 1][0], li[k + 1][1]

n = int(input())
li, minimum = [0] * n, [0] * n
count = 0

# list 입력
for i in range(0, n):
    li[i] = list(map(int, input().split()))

li.sort()
visited = [0] * (li[len(li) - 1][1])

# 회의 최소 시간 찾기
for i in range(0, len(li)):
    minimum[i] = li[i][1] - li[i][0]

for i in range(0, n):
    indexNum = minimum.index(min(minimum))
    tmp1, tmp2 = li[indexNum][0], li[indexNum][1]
    del li[tmp1]
    # popList(indexNum)

    minimum.pop(indexNum)

    for k in range(tmp1, tmp2):
        if visited[k] == 1:
            break
        elif k == (tmp2 - 1):
            for g in range(tmp1, tmp2):
                visited[g] = 1
                if g == (tmp2 - 1):
                    count += 1

print(count)       




    
