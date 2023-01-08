import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

global cnt
global relationiship
global visit
relationship = []
visit = [False] * (n + 1)
cnt = 0
visit[0] = True

for i in range(0, n + 1):
    relationship.append(list([0]))
for i in range(0, m):
    tmp1, tmp2 = map(int, input().split())
    relationship[tmp1].append(tmp2)
    relationship[tmp2].append(tmp1)

def friend(num):
    global cnt
    for g in range(1, len(relationship[num])):
        if visit[relationship[num][g]] == False:
            cnt += 1
            visit[relationship[num][g]] = True
            friend(relationship[num][g])
        else:
            continue
    return
    
friend(1)
print(cnt)
    