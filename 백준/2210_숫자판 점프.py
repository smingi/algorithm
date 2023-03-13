# 백준 2210_숫자판 점프

import sys


def dfs(r, c, cnt, result):
    result += str(board[r][c])

    if cnt == 6:
        lst.add(result)
        return

    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        new_r = r + dr
        new_c = c + dc

        if 0 <= new_r < 5 and 0 <= new_c < 5:
            dfs(new_r, new_c, cnt+1, result)


board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
lst = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, "")

print(len(lst))
