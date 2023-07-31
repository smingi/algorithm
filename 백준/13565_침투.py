# 백준 13565_침투

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    q.append([r, c])

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < M and 0 <= new_c < N and not board[new_r][new_c] and not visited[new_r][new_c]:
                visited[new_r][new_c] = 2
                q.append([new_r, new_c])


M, N = map(int, sys.stdin.readline().split())  # M: 행, N: 열
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

for j in range(N):
    if not board[0][j] and not visited[0][j]:
        visited[0][j] = 2
        bfs(0, j)

if visited[M-1].count(2):
    print('YES')
else:
    print('NO')
