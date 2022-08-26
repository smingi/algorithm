# 백준 7576_토마토


from collections import deque


def bfs():
    q = deque(ripe_tomatoes)

    while q:
        r, c, day = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] == 0:
                q.append([nr, nc, day+1])
                tomatoes[nr][nc] = day


M, N = map(int, input().split())  # M: 가로크기 N: 새로크기
tomatoes = [list(map(int, input().split())) for _ in range(N)]  # 현재 토마토 상태

ripe_tomatoes = []  # 익은 토마토 위치
days = 0  # 총 걸리는 일수

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:  # 현재 익은 토마토
            ripe_tomatoes.append([i, j, 1])
        if tomatoes[i][j] == 0:  # 익을 토마토가 있는지 체크
            days = 1

if days == 1:  # 익을 토마토가 있으면 실행
    bfs()
    days = max(map(max, tomatoes))  # 가장 늦게 익은 토마토의 날짜

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:  # 안익은 토마토가 있으면 -1
                days = -1
                break

print(days)

