import sys
input = sys.stdin.readline

def stick(x):
    origin = 64 
    sum = 0
    cnt = 0
    # 구할 막대기의 길이가 전체 합보다 작을!경우 -> 같으면 안 됨!! 같으면 빠져나와야 함!
    while sum < x:  
        # 구할 막대기 길이가 64면 origin을 반 나누기 전에 확인해야 함 
        if origin == x:
            return 1
        # 막대기를 반으로 나눠 다시 저장!  
        origin = origin/2
        # sum에 자른 막대기를 더했을 때 x보다 작으면 카운팅, sum에 자른 막대기 더하기
        if origin + sum  <= x:
            cnt += 1
            sum += origin
        # 자른 막대기를 sum에 더했을 때 x보다 크면 더 잘라야 함
        else:
            continue
    return cnt

print(stick(int(input())))