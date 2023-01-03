import sys
input = sys.stdin.readline

res = ""
for i in range(int(input())):
    li = list(map(int, input().split()))
    mean = (sum(li)-li[0])/li[0]
    cnt = 0
    for k in range(1, li[0]+1):
        if li[k] > mean:
             cnt += 1 
    res += str("{:.3f}%".format(cnt / (len(li)-1) * 100)) +"\n"
print(res)
    # res += str(round(cnt / (len(li)-1) * 100, 3)) + "%\n" 