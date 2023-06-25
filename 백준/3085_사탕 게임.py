# 백준 3085_사탕 게임

import sys


# 사탕 개수 찾기
def find_candy_cnt():
    max_cnt = 1

    for i in range(N):
        row_cnt = 1
        col_cnt = 1

        for j in range(1, N):
            # 행
            if board[j][i] == board[j - 1][i]:
                row_cnt += 1
            else:
                row_cnt = 1

            # 열
            if board[i][j] == board[i][j - 1]:
                col_cnt += 1
            else:
                col_cnt = 1

            max_cnt = max(max_cnt, row_cnt, col_cnt)

    return max_cnt


N = int(sys.stdin.readline().strip())  # 보드의 크기
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        # 행
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            result = max(result, find_candy_cnt())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

        # 열
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            result = max(result, find_candy_cnt())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

print(result)
