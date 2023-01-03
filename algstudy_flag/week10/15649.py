from calendar import c
from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


sen = ""
li = [k for k in range(1, n + 1)]
per = list(permutations(li, m))
sen = str(per)
tmp = 0
ans =""
enter = 1
for i in range(len(sen)):
    try:
        tmp = int(sen[i])
    except ValueError:
        pass
        continue
    
    except TypeError:
        pass
        continue
    if type(tmp) is int and tmp != 0:
        ans += str(tmp)
        if enter == m: 
            ans += "\n"
            enter = 1
        else:
            ans += " "
            enter += 1

    
print(ans)




#backtracking answer
# n, m = map(int, input().split())

# s = []
# def f():
#   if len(s) == m:
#     print(' '.join(map(str, s)))
#     return

#   for i in range(1, n + 1):
#     if i in s:
#       continue
#     s.append(i)
#     f()
#     s.pop()

# f()