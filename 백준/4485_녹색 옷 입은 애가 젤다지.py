# 백준 4485_녹색 옷 입은 애가 젤다지?

import sys
from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    cost[0][0] = board[0][0]

    while q:
        r, c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = r + dr
            new_c = c + dc

            if 0 <= new_r < N and 0 <= new_c < N:
                if cost[new_r][new_c] > cost[r][c] + board[new_r][new_c]:
                    cost[new_r][new_c] = cost[r][c] + board[new_r][new_c]
                    q.append([new_r, new_c])


index = 0
while True:
    N = int(sys.stdin.readline().strip())  # N*N

    if N == 0:
        break

    index += 1
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cost = [[150000] * N for _ in range(N)]

    bfs()

    print("Problem {}: {}".format(index, cost[N-1][N-1]))
