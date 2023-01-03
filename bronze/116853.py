import sys
input = sys.stdin.readline

n = int(input())
sen = ""

while n != 1:
    for i in range(2, n + 1):
        if n % i == 0:
            sen += (str(i) + "\n")
            n = int(n/i)
            break
    
print(sen.rstrip())
