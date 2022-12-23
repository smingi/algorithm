# 백준 14502_연구소


import sys
from itertools import combinations
from collections import deque


def check():  # 벽을 3개 세웠을 경우 안전한 공간 구하기
    global max_value
    for tr, tc in virus:
        if not temp_board[tr][tc]:
            bfs(tr, tc)

    virus_cnt = 0  # 바이러스 개수 구하기
    for i in range(N):
        virus_cnt += temp_board[i].count(2)

    safe_cnt = (N*M) - virus_cnt - w_len  # 안전지역 개수

    if safe_cnt > max_value:
        max_value = safe_cnt


def bfs(r, c):  # 너비우선 탐색으로 바이러스에 감염되는 부분과 벽, 안전한 공간 체크
    q = deque()
    q.append([r, c])
    temp_board[r][c] = 2

    while q:
        pr, pc = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = pr + dr
            nc = pc + dc

            if 0 <= nr < N and 0 <= nc < M and not temp_board[nr][nc]:
                if board[nr][nc] == 1:
                    temp_board[nr][nc] = 1
                else:
                    q.append([nr, nc])
                    temp_board[nr][nc] = 2


N, M = map(int, sys.stdin.readline().split())  # N: 세로, M: 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 연구소 상태(0: 빈 칸, 1: 벽, 2: 바이러스)

virus = []  # 바이러스 위치
wall = []  # 벽 위치
empty = []  # 빈 칸 위치

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append([i, j])
        elif board[i][j] == 1:
            wall.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

w_len = len(wall) + 3  # 벽 개수
max_value = 0  # 최대 안전 지역 개수

for combi in combinations(empty, 3):  # 완전 탐색
    temp_board = [[0] * M for _ in range(N)]  # 임시 상태(벽 3개 추가)
    for combi_r, combi_c in combi:
        temp_board[combi_r][combi_c] = 1
    check()
    for combi_r, combi_c in combi:
        temp_board[combi_r][combi_c] = 0

print(max_value)  # 최대 안전 지역 개수 출력
