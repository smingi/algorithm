# 백준 2178 미로 탐색


def prim():
    D[0][0] = 1
    q = []
    q.append((0, 0, 1))
    while q:
        i, j, cnt = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj]:
                if D[ni][nj] > cnt:
                    D[ni][nj] = cnt
                    q.append((ni, nj, cnt+1))


N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]
D = [[987654321] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not lst[i][j]:
            D[i][j] = 0
prim()
print(D[N-1][M-1]+1)
