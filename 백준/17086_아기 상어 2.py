# 백준 17086_아기 상어 2

import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())  # N: 세로, M: 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if board[i][j]:
            q.append([i, j])

while q:
    r, c = q.popleft()

    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        new_r = r + dr
        new_c = c + dc

        if 0 <= new_r < N and 0 <= new_c < M and not board[new_r][new_c]:
            board[new_r][new_c] = board[r][c] + 1
            q.append([new_r, new_c])

print(max(map(max, board)) - 1)
