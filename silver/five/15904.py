import sys
input = sys.stdin.readline

compare = list("UCPC")
sen = input().rstrip()

for i in range(0, len(sen)):
    if sen[i] == compare[0]:
        compare.pop(0)
        if len(compare) == 0:
            break
    
if len(compare) == 0:
    print("I love UCPC")
else:
    print("I hate UCPC")
