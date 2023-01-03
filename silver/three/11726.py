import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[n])


# import sys
# import math
# input = sys.stdin.readline
# fact = math.factorial
# num = int(input())
# sum = 0

# for width in range(0, int(num/2) + 1):
#     height = num - width * 2
#     sum += fact(height + width)/(fact(height) * fact(width))
#     sum = math.trunc(sum)%10007
# print((math.trunc(sum))%10007)