import sys
input = sys.stdin.readline

order = input().split()

result = ""
while int(order[0]) != 0 or int(order[1]) != 0:
    if int(order[0]) > int(order[1]):
        result += "Yes\n"
    else:
        result += "No\n"
    order = input().split()
print(result.rstrip())