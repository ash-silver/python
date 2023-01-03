import sys
input = sys.stdin.readline

global e, s, m
e, s, m = map(int, input().split())
cnt = 1

def m():
    m -= (s - 1)
    if m < 0 : 
        m += 19
        
def e():
    e -= (s - 1)
    if e < 0:
        e += 15


while e != 1 or s != 1 or m != 1:
    m()
    e()
    cnt += s
    s -= (s - 1)

print(cnt)
