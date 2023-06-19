# 백준 3184_양

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    # 양과 늑대의 수
    sheep, wolf = 0, 0

    while q:
        now_r, now_c = q.popleft()

        # 양인 경우
        if board[now_r][now_c] == 'o':
            sheep += 1

        # 늑대인 경우
        if board[now_r][now_c] == 'v':
            wolf += 1

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < R and 0 <= new_c < C and not visited[new_r][new_c] and board[new_r][new_c] != '#':
                q.append([new_r, new_c])
                visited[new_r][new_c] = 1

    if sheep and wolf:
        if sheep > wolf:
            wolf = 0
        else:
            sheep = 0

    return sheep, wolf


R, C = map(int, sys.stdin.readline().split())  # R: 행, C: 열
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 총 양과 늑대의 수
total_sheep, total_wolf = 0, 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j] != '#':
            result_sheep, result_wolf = bfs(i, j)
            total_sheep += result_sheep
            total_wolf += result_wolf

print(total_sheep, total_wolf)
