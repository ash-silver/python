import sys
input = sys.stdin.readline

li = []
for i in range(0, 5):
    li.append(int(input()))
li.sort()
print(round(sum(li)/5))
print(li[2])