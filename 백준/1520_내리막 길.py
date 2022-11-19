# 백준 1520_내리막 길

import sys
sys.setrecursionlimit(10**6)


def dfs(r, c):
    if r == M-1 and c == N-1:  # 도착지에 도착한 경우
        return 1

    if dp[r][c] != -1:  # 한번이라도 방문한 경우
        return dp[r][c]

    dp[r][c] = 0  # 방문하지 않은 경우 0부터 시작
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < M and 0 <= nc < N and board[r][c] > board[nr][nc]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c]


M, N = map(int, sys.stdin.readline().split())  # M: 새로, N: 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  # 지도
dp = [[-1] * N for _ in range(M)]

print(dfs(0, 0))
