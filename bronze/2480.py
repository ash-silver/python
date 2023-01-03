import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# a = b
if a == b :
    # a = b = c
    if b == c:
        print(10000 + a * 1000)
    # a = b != c
    else :
        print(1000 + a * 100)
# a = c
elif a == c:
    print(1000 + a * 100)

elif b == c:
    print(1000 + 100 * b)

else: 
    print(max(max(a, b), c) * 100)