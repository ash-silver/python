import sys
input = sys.stdin.readline

num = input()
cnt = 0
li = []

while 1:
    for a in range(0, 9):
        for d in range(0, 9):
            li = []
            for n in range(1, len(num) + 1):
                li.append(int(a + ((n-1) * d)))
                
            print(li)
            if sum(int(li)) > num:
                break
