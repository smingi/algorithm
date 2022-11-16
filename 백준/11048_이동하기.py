# 백준 11048_이동하기

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 세로, M: 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 사탕개수
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N][M])
