# 백준 14716_현수막

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    q.append([r, c])
    board[r][c] = 0

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < M and 0 <= new_c < N and board[new_r][new_c]:
                q.append([new_r, new_c])
                board[new_r][new_c] = 0


M, N = map(int, sys.stdin.readline().split())  # M: 행, N: 열
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
result = 0

for i in range(M):
    for j in range(N):
        if board[i][j]:
            result += 1
            bfs(i, j)

print(result)
