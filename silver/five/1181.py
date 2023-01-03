import sys
input = sys.stdin.readline

word = list(set([input().rstrip() for _ in range(int(input()))]))
word.sort()
word.sort(key=lambda x:len(x))
for i in range(len(word)):
    print(word[i])