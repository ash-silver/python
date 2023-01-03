import sys
input = sys.stdin.readline

n, k = map(int, input().split())

global li
li = list(set(i for i in range(2, n + 1)))

for i in range(0, len(li)):
    for g in range(i + 1, len(li)):
        if g >= len(li):
            break
        if li[g] % li[i] == 0:
            tmp = li[g]
            li.remove(li[g])
            k  -= 1
        elif g == len(li) - 1:
            li.remove(li[0])
            tmp = li[0]
            k -= 1
print(tmp)


    
        
                    
        



