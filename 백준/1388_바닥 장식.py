# 백준 1388_바닥 장식

import sys


def check(r, c, shape):
    if shape == '-':
        for col in range(c+1, M):
            if board[r][col] == '-':
                visited[r][col] = 1
            else:
                return

    else:
        for row in range(r+1, N):
            if board[row][c] == '|':
                visited[row][c] = 1
            else:
                return


N, M = map(int, sys.stdin.readline().split())  # N: 세로, M: 가로
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            result += 1
            check(i, j, board[i][j])

print(result)
