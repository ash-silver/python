from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
li = deque()
result, cnt = "", 0


for i in range(0, n):
    order = input().split()
    if order[0] == "push":
        li.append(order[1])
        cnt += 1

    elif order[0] == "pop":
        if cnt == 0:
            result += "-1"
        else:
            result += str(li.popleft()) 
            cnt -= 1
        result += "\n"

    elif order[0] == "size":
        result += str(cnt)
        result += "\n"
    
    elif order[0] == "empty":
        if cnt == 0:
            result += "1" 
        else : 
            result += "0" 
        result += "\n"
    
    elif order[0] == "front":
        if cnt == 0:
            result += "-1" 

        else :
            result += str(li[0]) 
        result += "\n"
    
    elif order[0] == "back":
        if cnt == 0:
            result += "-1" 
            
        else : 
            result += str(li[cnt - 1]) 
        result += "\n"

result = result.rstrip()
print(result)

