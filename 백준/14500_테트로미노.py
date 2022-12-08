# 백준 14500_테트로미노

import sys


def dfs(r, c, cnt, sumv):
    global maxv

    if maxv >= sumv + max_num * (3-cnt):  # 가지치기
        return

    if cnt == 3:  # 4개 다 선택한 경우
        if sumv > maxv:
            maxv = sumv
        return

    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if cnt == 1:  # 산모양 예외 처리
                visited[nr][nc] = 1
                dfs(r, c, cnt+1, sumv+paper[nr][nc])
                visited[nr][nc] = 0
            visited[nr][nc] = 1
            dfs(nr, nc, cnt+1, sumv + paper[nr][nc])
            visited[nr][nc] = 0


N, M = map(int, sys.stdin.readline().split())  # N: 새로, M: 가로
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 종이에 적힌 수

visited = [[0] * M for _ in range(N)]
max_num = max(map(max, paper))  # 가장 큰 숫자
maxv = 0  # 최댓값

for i in range(N):  # 완전탐색
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, paper[i][j])
        visited[i][j] = 0

print(maxv)
