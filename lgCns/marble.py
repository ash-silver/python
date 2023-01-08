from itertools import combinations, product
import sys
input = sys.stdin.readline

li = list(input().split())

def first(li):
    if len(li) % 2 == 0:
        tmpa = sum(li[:len(li)/2 -1])
        tmpb = sum(li[len(li)/2:])
        if tmpa != tmpb:
            return False
    else:
        tmpa = sum(li[0:int(len(li)/2)])
        tmpb = sum(li[len(li)/2 + 1:0])
        if tmpa != tmpb:
            return False
    return True
#  def second(li):
for i in range(len(li) - 1, 0, -1):
    comLi = list(combinations(li, i + 1))
    comLi.sort(reverse=True)
    # print(comLi)   
    for k in range(len(comLi) - 1, 0, -1):
        tmp = comLi[k]
        tmpLi = list()
        for g in range(0, len(tmp)):    
            tmpLi.append(int(tmp[g]))    
        tmpLi = list(combinations(li, len(tmpLi)))
        for g in range(0, len(tmpLi)):
            if first(tmpLi) == False:
                continue
            print(tmpLi)



