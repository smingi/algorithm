# 백준 1051_숫자 정사각형

import sys


def find_square():
    for s in range(min(N, M), 0, -1):
        for i in range(N - s + 1):
            for j in range(M - s + 1):
                if board[i][j] == board[i][j+s-1] == board[i+s-1][j] == board[i+s-1][j+s-1]:
                    return s*s

    return 1


N, M = map(int, sys.stdin.readline().split())  # N: 행, M: 열
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
print(find_square())
