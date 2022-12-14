# 백준 4963_섬의 개수

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    q.append([r, c])
    board[r][c] = 2

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < h and 0 <= new_c < w and board[new_r][new_c] == 1:
                q.append([new_r, new_c])
                board[new_r][new_c] = 2


while True:
    w, h = map(int, sys.stdin.readline().split())  # w: 너비, h: 높이

    if w == 0 and h == 0:  # 종료조건
        break

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]  # 지도 정보
    cnt = 0  # 섬의 개수

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)
