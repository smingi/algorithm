# 백준 1987_알파벳

import sys


def bfs():
    q = set()  # 중복방지를 위해 set 사용
    q.add((0, 0, board[0][0]))  # 시작지점
    max_move = 0  # 최대 이동 횟수

    while q:
        r, c, lst = q.pop()  # 행, 열, 방문한 알파벳 리스트
        max_move = max(max_move, len(lst))  # 최대 이동 횟수 저장

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in lst:
                q.add((nr, nc, lst + board[nr][nc]))

    print(max_move)


R, C = map(int, sys.stdin.readline().split())  # R: 행, C: 열
board = [list(sys.stdin.readline().strip()) for _ in range(R)]  # 보드판

bfs()
