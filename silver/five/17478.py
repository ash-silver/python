import sys
input = sys.stdin.readline

n = int(input())
global under
under = "____"

recurPrint = [
    "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.",
    "\"재귀함수가 뭔가요?\"",
    "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.",
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
    "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"",
    "\"재귀함수는 자기 자신을 호출하는 함수라네\"",
    "라고 답변하였지."
]

cnt = 0
def printUnder(cnt):
    for i in range(cnt):
        print("____", end ="")

# 맨 처음 호출되는 것
print(recurPrint[0])
# 재귀함수가 뭐야~
printUnder(cnt)
print(recurPrint[1])


# 재귀함수 시작
def recur(cnt):
    if cnt >= n:
# 교수님 마지막 답변
        printUnder(cnt)
        print(recurPrint[5])
# 라고 답변~
        printUnder(cnt)
        print(recurPrint[6])
        return

# 교수님 답변1
    printUnder(cnt)
    print(recurPrint[2])
# 교수님 답변2
    printUnder(cnt)
    print(recurPrint[3])
# 교수님 답변3
    printUnder(cnt)
    print(recurPrint[4])
    cnt += 1
    printUnder(cnt)
    print(recurPrint[1])
    recur(cnt)

# 교수님 마지막 답변
    cnt -= 1
    printUnder(cnt)
    print(recurPrint[6])

recur(cnt)