# 백준 1003 피보나치 함수


lst = [[] for _ in range(41)]  # 미리 구하기
lst[0] = [1, 0]
lst[1] = [0, 1]
lst[2] = [1, 1]
for i in range(3, 41):
    lst[i] = [lst[i-1][1], lst[i-1][0] + lst[i-1][1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(lst[N][0], lst[N][1])
