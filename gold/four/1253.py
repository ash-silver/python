import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()
cnt = 0

def search(num):
    global cnt
    global li
    li.remove(num)
    i = 0
    k = n - 2
    while i < k:
        sum = li[i] + li[k]
        if sum > num:
            k -= 1
        elif sum < num:
            i += 1
        else: 
            cnt += 1
            break
    li.append(num)
    li.sort()

for i in li:
    search(i)
print(cnt)