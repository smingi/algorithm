# 백준 2468_안전 영역

import sys
from collections import deque


def bfs(r, c, h):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] > h and not visited[new_r][new_c]:
                q.append([new_r, new_c])
                visited[new_r][new_c] = 1


N = int(sys.stdin.readline().strip())  # N*N 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 지도정보
max_height = max(map(max, board))  # 최대 높이
max_cnt = 0  # 최대 영역의 개수

for height in range(max_height):
    visited = [[0] * N for _ in range(N)]
    cnt = 0  # 영역의 개수

    for i in range(N):
        for j in range(N):
            if board[i][j] > height and not visited[i][j]:
                cnt += 1
                bfs(i, j, height)

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
