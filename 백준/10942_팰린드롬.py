# 백준 10942_팰린드롬?

import sys


N = int(sys.stdin.readline().strip())  # 자연수의 개수
sequence = list(map(int, sys.stdin.readline().split()))  # 수열

# 질문전에 미리 계산
dp = [[0] * N for _ in range(N)]
dp[N-1][N-1] = 1
for i in range(N-1):
    # 1자리인 경우
    dp[i][i] = 1

    # 2자리인 경우
    if sequence[i] == sequence[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

# 3자리 이상인 경우
for i in range(N-2):  # 3 + i 자리
    for start in range(N-2-i):
        end = i+start+2
        if sequence[start] == sequence[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1

M = int(sys.stdin.readline().strip())  # 질문횟수
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())  # S ~ E
    print(dp[S-1][E-1])
