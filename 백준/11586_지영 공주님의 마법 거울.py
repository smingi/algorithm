# 백준 11586 지영 공주님의 마법 거울


N = int(input())
lst = [input() for _ in range(N)]  # 입력받은 정보
K = int(input())  # 심리상태

if K == 1:  # 그대로
    for i in range(N):
        print(lst[i])

elif K == 2:  # 좌우 반전
    for i in range(N):
        print(lst[i][::-1])

else:  # 상하 반전
    for i in range(N):
        print(lst[N-1-i])
