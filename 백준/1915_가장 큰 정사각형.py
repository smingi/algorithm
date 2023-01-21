# 백준 1915_가장 큰 정사각형

import sys


n, m = map(int, sys.stdin.readline().split())  # n: 행, m: 열
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]  # 보드판

for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == 1:
            board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

max_size = max(map(max, board))  # 가장 큰 정사각형의 크기
print(max_size ** 2)  # 가장 큰 정사각형의 넓이
