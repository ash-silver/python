import sys
input = sys.stdin.readline

sen = input()
res = ""

li = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'O', 'U', 'E']
while sen != "#\n":
    cnt = 0
    for i in range(0, len(sen)):
        if sen[i] in li:
            cnt += 1
    res += (str(cnt) + "\n")
    sen = input()

print(res)
