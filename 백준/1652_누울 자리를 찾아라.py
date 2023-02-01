# 백준 1652_누울 자리를 찾아라

import sys


N = int(sys.stdin.readline().strip())  # N*N
board = [list(sys.stdin.readline().strip()) for _ in range(N)]  # 보드판
row, col = 0, 0

for i in range(N):
    row_length, col_length = 0, 0

    for j in range(N):
        if board[i][j] == ".":
            row_length += 1

        else:
            row_length = 0

        if row_length == 2:
            row += 1

        if board[j][i] == ".":
            col_length += 1

        else:
            col_length = 0

        if col_length == 2:
            col += 1

print(row, col)
