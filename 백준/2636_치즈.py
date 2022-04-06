# 백준 2636 치즈


def bfs(i, j):  # bfs(겉부분 치즈 제거하는 함수)
    visited = [[0]*M for _ in range(N)]
    global cheese
    q = []
    q.append((i, j))
    while q:
        r, c = q.pop(0)
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = 1
                if lst[nr][nc]:  # 치즈 녹이기
                    lst[nr][nc] = 0
                    cheese -= 1
                else:  # 녹인 부분이 아니면 다음위치로 이동
                    q.append((nr, nc))


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cheese = 0  # 치즈 개수
time = 0  # 걸린 시간
for i in range(N):
    for j in range(M):
        if lst[i][j]:
            cheese += 1
while cheese:
    cnt = cheese
    bfs(0, 0)
    time += 1

print(time)
print(cnt)
