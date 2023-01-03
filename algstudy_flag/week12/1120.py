import sys
input = sys.stdin.readline

a,b = input().split()
# a와 b에서 입력받은 것을 한 글자씩 리스트 a와 b에 저장
listA, listB = list(a), list(b)                      
minimum = len(listA)

# 첫 번째 부분부터 listB와 listA길이의 차까지 전부 다 해 보기 -> Brute Force
for k in range(0, len(listB)-len(listA)+1):
    tmp = len(listA)
    # listA 첫 부분부터 일치하는지 확인
    for i in range(0, len(listA)):
        # 같으면 tmp에서 빼기
        if listA[i] == listB[i+k]:
            tmp -= 1
    minimum = min(minimum, tmp)

print(minimum)








# import sys
# input = sys.stdin.readline

# a,b = input().split()
# listA, listB = list(a), list(b)
# minimum = len(listA)

# # 두 문자열의 길이가 같을 경우
# if len(listA) == len(listB):
#     for i in range(0, len(listA)):
#         if listA[i] == listB[i]:
#             minimum -= 1
# # 두 문자열의 길이가 다를 경우
# else:
# # listB의 어디서부터 시작할지 위치 선정
#     for k in range(0, len(listB)-len(listA)+1):
#         tmp = len(listA)
#         # listA 첫 부분부터 일치하는지 확인
#         for i in range(0, len(listA)):
#             if listA[i] == listB[i+k]:
#                 tmp -= 1
#         minimum = min(minimum, tmp)

# print(minimum)


