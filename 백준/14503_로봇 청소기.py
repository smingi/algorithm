# 백준 14503 로봇 청소기

import sys
sys.setrecursionlimit(10**6)


# d: 0, 1, 2, 3 -> 북, 동, 남, 서
def move(r, c, d, block):
    global cnt

    if block == 4:  # 후진
        if d == 0:  # 보는 방향: 북쪽
            nr = r+1
            nc = c
        elif d == 1:  # 보는 방향: 동쪽
            nr = r
            nc = c-1
        elif d == 2:  # 보는 방향: 남쪽
            nr = r-1
            nc = c
        elif d == 3:  # 보는 방향: 서쪽
            nr = r
            nc = c+1
        if 0 <= nr < N and 0 <= nc < M:
            if lst[nr][nc] != 1:  # 벽이 아닐 때만 후진
                lst[nr][nc] = 2
                move(nr, nc, d, 0)
        return

    if d == 0:  # 보는 방향: 북쪽
        nr = r
        nc = c-1
    elif d == 1:  # 보는 방향: 동쪽
        nr = r-1
        nc = c
    elif d == 2:  # 보는 방향: 남쪽
        nr = r
        nc = c+1
    elif d == 3:  # 보는 방향: 서쪽
        nr = r+1
        nc = c

    if 0 <= nr < N and 0 <= nc < M:
        nd = d - 1  # 방향조절
        if nd < 0:
            nd = 3
        if not lst[nr][nc]:
            lst[nr][nc] = 2  # 청소표시
            cnt += 1  # 개수 증가
            move(nr, nc, nd, 0)
        else:
            move(r, c, nd, block+1)


N, M = map(int, input().split())  # N: 새로, M: 가로
sr, sc, d = map(int, input().split())  # 시작행, 시작열, 방향
lst = [list(map(int, input().split())) for _ in range(N)]
lst[sr][sc] = 2  # 2는 청소한 곳
cnt = 1  # 청소한 장소 개수
move(sr, sc, d, 0)
print(cnt)
