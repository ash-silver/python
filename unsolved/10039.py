import sys
input = sys.stdin.readline

li = [int(input()) for i in range(0, 5)]
for i in range(0, len(li)):
    if  li[i] < 40 :
        li[i] = 40
print(int(sum(li)/5))