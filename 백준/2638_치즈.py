# 백준 2638_치즈

from collections import deque


def find_start():  # 시작 위치 찾기
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and cheese[i][j] == 0 and (i == 0 or i == N - 1) or (j == 0 or j == M - 1):
                melt_cheese(i, j)
                return


def melt_cheese(r, c):  # 녹는 치즈 찾기
    q = deque()
    q.append([r, c])
    visited[r][c] = 1

    while q:
        pr, pc = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = pr + dr
            nc = pc + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if cheese[nr][nc] >= 1:  # 치즈인 경우 +1로 표시
                    cheese[nr][nc] += 1
                else:  # 공기인 경우 방문표시하고 이동
                    visited[nr][nc] = 1
                    q.append([nr, nc])


N, M = map(int, input().split())   # N: 세로, M: 가로
cheese = [list(map(int, input().split())) for _ in range(N)]  # 치즈 상태
time = 0  # 걸린 시간

while True:
    go = False  # 계속 탐색할 건지 여부
    visited = [[0] * M for _ in range(N)]
    find_start()  # 녹일 치즈 찾기

    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 3:  # 2번 이상 노출되면 3이상이 됨
                cheese[i][j] = 0  # 치즈 녹이기
                go = True  # 치즈가 녹았으므로 탐색 한번 더

            elif cheese[i][j] == 2:  # 2이면 1번만 노출된 경우
                cheese[i][j] = 1  # 다시 1로 원상복귀

    if go:  # 치즈가 녹았으면 시간 +1
        time += 1

    else:  # 녹은 치즈가 없으면 종료
        break

print(time)
