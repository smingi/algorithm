# 백준 7569_토마토


from collections import deque


def bfs():  # 토마토 익히기
    q = deque(ripe_tomatoes)

    while q:
        h, r, c = q.popleft()  # h: 높이, r: 행, c: 열
        day = tomatoes[h][r][c]  # 걸린시간

        for dh, dr, dc in [[-1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1]]:
            nh = h + dh  # 높이 이동
            nr = r + dr  # 행 이동
            nc = c + dc  # 열 이동

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if tomatoes[nh][nr][nc] == 0:  # 안익은 토마토 익히기
                    tomatoes[nh][nr][nc] = day+1
                    q.append([nh, nr, nc])


def check():  # 다 익었는지 확인
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 0:  # 토마토가 안익은 경우
                    return False

    return True


M, N, H = map(int, input().split())  # M: 가로 N: 새로 H: 높이
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

ripe_tomatoes = []  # 익은 토마토 위치

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:  # 익어있는 토마토 위치
                ripe_tomatoes.append([i, j, k])


if ripe_tomatoes:  # 익은 토마토가 있는 경우
    bfs()

if check():  # 다 익었는지 확인
    days = 0  # 다 익는 날짜
    for i in range(H):
        maxv = max(map(max, tomatoes[i]))
        if days < maxv:
            days = maxv
    print(days-1)

else:
    print(-1)  # 다 안익으면 -1
