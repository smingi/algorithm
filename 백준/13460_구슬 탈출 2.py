# 백준 13460_구슬 탈출 2

import sys
from collections import deque


def move(now_r, now_c, dr, dc):  # 이동하기 (현재 행, 현재 열, 방향(행, 열)
    move_cnt = 0  # 움직인 거리

    # 벽이 아니고 구멍에 빠지지 않을 때까지 이동
    while board[now_r + dr][now_c + dc] != "#" and board[now_r][now_c] != "O":
        now_r += dr
        now_c += dc
        move_cnt += 1

    return now_r, now_c, move_cnt


def bfs():
    q = deque()
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    q.append([red_r, red_c, blue_r, blue_c, 1])
    visited[red_r][red_c][blue_r][blue_c] = 1

    while q:
        now_red_r, now_red_c, now_blue_r, now_blue_c, cnt = q.popleft()

        if cnt > 10:  # 10번 시도해도 구멍을 못찾은 경우 종료
            return -1

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_red_r, new_red_c, red_cnt = move(now_red_r, now_red_c, dr, dc)
            new_blue_r, new_blue_c, blue_cnt = move(now_blue_r, now_blue_c, dr, dc)

            if board[new_blue_r][new_blue_c] != "O":  # 파란 구슬을 구멍에 넣지 않고
                if board[new_red_r][new_red_c] == "O":  # 빨간 구슬만 구멍에 넣은 경우 종료
                    return cnt

                # 빨간 구슬과 파란 구슬의 위치가 곂치는 경우 위치 조정
                if new_red_r == new_blue_r and new_red_c == new_blue_c:
                    if red_cnt > blue_cnt:
                        new_red_r -= dr
                        new_red_c -= dc
                    else:
                        new_blue_r -= dr
                        new_blue_c -= dc

                # 이전에 왔던 위치가 아니라면 새롭게 탐색
                if not visited[new_red_r][new_red_c][new_blue_r][new_blue_c]:
                    visited[new_red_r][new_red_c][new_blue_r][new_blue_c] = 1
                    q.append([new_red_r, new_red_c, new_blue_r, new_blue_c, cnt+1])

    return -1  # 찾지 못한 경우 -1


N, M = map(int, sys.stdin.readline().split())  # N: 세로, M: 가로
board = [list(sys.stdin.readline().strip()) for _ in range(N)]  # 보드의 상태
red_r, red_c = 0, 0  # 빨간공의 위치
blue_r, blue_c = 0, 0  # 파란공의 위치

# 공 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            red_r, red_c = i, j

        elif board[i][j] == "B":
            blue_r, blue_c = i, j

print(bfs())
