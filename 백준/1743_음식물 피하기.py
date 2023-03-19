# 백준 1743_음식물 피하기

import sys
from collections import deque


def bfs(rr, cc):
    global result
    q = deque()
    q.append([rr, cc])
    visited[rr][cc] = 1
    cnt = 1

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < N and 0 <= new_c < M:
                if board[new_r][new_c] and not visited[new_r][new_c]:
                    q.append([new_r, new_c])
                    visited[new_r][new_c] = 1
                    cnt += 1

    return cnt


N, M, K = map(int, sys.stdin.readline().split())  # 세로, 가로, 음식물 개수
board = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())  # 음식물 위치
    board[r-1][c-1] = 1

visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] and not visited[i][j]:
            result = max(result, bfs(i, j))

print(result)
