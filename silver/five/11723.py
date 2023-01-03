import sys
input = sys.stdin.readline

result = ""
m = int(input())
s = [False] * 21
order = dict()

for i in range(0, m):
    order = input().split()
    if order[0] == "add":
        if s[int(order[1])] == False:
            s[int(order[1])] = True
    
    elif order[0] == "remove":
        s[int(order[1])] = False

    elif order[0] == "check":
        if s[int(order[1])] == True :
            print("1")
        else :
            print("0")

    elif order[0] == "toggle":
        if s[int(order[1])] == True:
            s[int(order[1])] = False
        else:
            s[int(order[1])] = True

    elif order[0] == "all":
        s = [True] * 21

    elif order[0]== "empty":
        s = [False] * 21