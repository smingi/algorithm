# 백준 3055_탈출

import sys
from copy import deepcopy
from collections import deque


def move_water():  # 물 이동
    global board
    new_board = deepcopy(board)

    for i in range(R):
        for j in range(C):
            if board[i][j] == "*":
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr = i + dr
                    nc = j + dc

                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "X" and board[nr][nc] != "D":
                        new_board[nr][nc] = "*"

    board = new_board


def move_beaver():  # 비버 이동
    q = deque()
    visited = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == "S":
                q.append([i, j, 0])
                visited[i][j] = 1
                break

    time = -1  # 시작 시간

    while q:
        now_r, now_c, minute = q.popleft()

        # 비버가 움직이기전에 물이 먼저 이동
        if time != minute:
            time = minute
            move_water()

        # 도착한 경우
        if board[now_r][now_c] == "D":
            return minute

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < R and 0 <= new_c < C and not visited[new_r][new_c]:
                if board[new_r][new_c] != "*" and board[new_r][new_c] != "X":
                    q.append([new_r, new_c, minute+1])
                    visited[new_r][new_c] = 1

    # 도착하지 못한 경우
    return "KAKTUS"


R, C = map(int, sys.stdin.readline().split())  # 행, 열
board = [list(sys.stdin.readline().strip()) for _ in range(R)]  # 지도상태
# .: 비어있는 곳, *: 물이 차있는 지역, X: 돌이 있는 곳, D: 비버의 굴, S: 고슴도치의 위치
print(move_beaver())
