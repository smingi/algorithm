# 백준 16724_피리 부는 사나이

import sys


def find_parent(r, c):  # 부모노드 찾기
    if parent[r][c] != [r, c]:
        parent[r][c] = find_parent(parent[r][c][0], parent[r][c][1])

    return parent[r][c]


def union(a_r, a_c, b_r, b_c):  # 연결하기
    p_a_r, p_a_c = find_parent(a_r, a_c)
    p_b_r, p_b_c = find_parent(b_r, b_c)

    parent[p_b_r][p_b_c] = [p_a_r, p_a_c]


def dfs(now_r, now_c):
    global cnt
    new_r, new_c = now_r, now_c

    # 상
    if board[now_r][now_c] == "U":
        new_r -= 1

    # 하
    elif board[now_r][now_c] == "D":
        new_r += 1

    # 좌
    elif board[now_r][now_c] == "L":
        new_c -= 1

    # 우
    elif board[now_r][now_c] == "R":
        new_c += 1

    p_now_r, p_now_c = find_parent(now_r, now_c)
    p_new_r, p_new_c = find_parent(new_r, new_c)

    if [p_now_r, p_now_c] != [p_new_r, p_new_c]:
        union(p_now_r, p_now_c, p_new_r, p_new_c)
        cnt -= 1
        dfs(new_r, new_c)


N, M = map(int, sys.stdin.readline().split())  # N: 행, M: 열
board = [list(sys.stdin.readline().strip()) for _ in range(N)]  # 지도정보
parent = [[[i, j] for j in range(M)] for i in range(N)]
cnt = N * M  # ‘SAFE ZONE’의 최소 개수

for i in range(N):
    for j in range(M):
        if parent[i][j] == [i, j]:
            dfs(i, j)

print(cnt)
