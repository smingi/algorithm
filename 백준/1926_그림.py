# 백준 1926_그림

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    visited[r][c] = 1
    width = 1
    q.append([r, c])

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < n and 0 <= new_c < m and board[new_r][new_c] and not visited[new_r][new_c]:
                visited[new_r][new_c] = 1
                width += 1
                q.append([new_r, new_c])

    return width


n, m = map(int, sys.stdin.readline().split())  # n: 세로, m: 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 보드판
visited = [[0] * m for _ in range(n)]
cnt = 0  # 그림의 개수
max_area = 0  # 가장 넓은 그림의 넓이

for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)
