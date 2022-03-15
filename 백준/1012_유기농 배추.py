# 백준 1012 유기농 배추


def bfs(i, j):  # 배추있는 곳만 탐색
    q = []
    q.append((i, j))
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1   # 배추 방문 표시
                q.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # M: 가로, N: 세로 K: 배추개수
    cabbage = [list(map(int, input().split())) for _ in range(K)]  # 배추 위치
    visited = [[1] * M for _ in range(N)]  # 배추있으면 0 없으면 1
    cnt = 0  # 필요한 벌레 개수

    for i in range(len(cabbage)):  # 배추위치 표시
        r = cabbage[i][1]
        c = cabbage[i][0]
        visited[r][c] = 0

    for i in range(len(cabbage)):  # 배추위치에서 dfs
        r = cabbage[i][1]
        c = cabbage[i][0]
        if not visited[r][c]:  # 간적없는 배추만 방문
            visited[r][c] = 1  # 배추 방문 표시
            bfs(r, c)
            cnt += 1  # 필요한 벌레 개수 추가

    print(cnt)
