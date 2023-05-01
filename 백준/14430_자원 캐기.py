# 백준 14430_자원 캐기

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 세로, M: 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            dp[i][j] = board[i][j]

        elif i > 0 and j > 0:
            dp[i][j] = board[i][j] + max(dp[i-1][j], dp[i][j-1])

        elif j == 0:
            dp[i][j] = board[i][j] + dp[i-1][j]

        elif i == 0:
            dp[i][j] = board[i][j] + dp[i][j-1]

print(dp[-1][-1])
