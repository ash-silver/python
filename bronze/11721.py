import sys
input = sys.stdin.readline

sen = input().rstrip()
for i in range(0, len(sen),10):
    print(sen[i:i + 10])