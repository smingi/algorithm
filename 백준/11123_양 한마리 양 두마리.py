# 백준 11123_양 한마리... 양 두마리...

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

            if 0 <= new_r < H and 0 <= new_c < W:
                if board[new_r][new_c] == "#" and not visited[new_r][new_c]:
                    q.append([new_r, new_c])
                    visited[new_r][new_c] = 1


T = int(sys.stdin.readline().strip())
for _ in range(T):
    H, W = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    result = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == '#' and not visited[i][j]:
                visited[i][j] = 1
                result += 1
                bfs(i, j)

    print(result)
