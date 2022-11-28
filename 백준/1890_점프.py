# 백준 1890_점프

import sys


N = int(sys.stdin.readline().strip())  # N*N 게임판
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 게임판
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1  # 시작지점

for i in range(N):
    for j in range(N):

        # 종료 지점
        if i == N-1 and j == N-1:
            print(dp[i][j])
            break

        # 아래쪽으로 이동
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]

        # 오른쪽으로 이동
        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]
