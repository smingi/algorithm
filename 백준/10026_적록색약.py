# 백준 10026_적록색약


from collections import deque


def normal(r, c, color):
    q = deque()
    q.append([r, c])
    normal_visited[r][c] = 1
    while q:
        pr, pc = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < N and 0 <= nc < N and not normal_visited[nr][nc] and colors[nr][nc] == color:
                q.append([nr, nc])
                normal_visited[nr][nc] = 1


def rg_color_blind(r, c, color):
    q = deque()
    q.append([r, c])
    rc_visited[r][c] = 1
    while q:
        pr, pc = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < N and 0 <= nc < N and not rc_visited[nr][nc]:
                if (color == "R" or color == "G") and (colors[nr][nc] == "R" or colors[nr][nc] == "G"):
                    q.append([nr, nc])
                    rc_visited[nr][nc] = 1
                elif color == "B" and colors[nr][nc] == color:
                    q.append([nr, nc])
                    rc_visited[nr][nc] = 1


N = int(input())  # N * N 범위
colors = [list(input()) for _ in range(N)]  # 보이는 색

normal_visited = [[0] * N for _ in range(N)]  # 정상의 체크 여부
rc_visited = [[0] * N for _ in range(N)]  # 적록생맹의 체크 여부
n_cnt = 0  # 정상의 구역 개수
rg_cnt = 0  # 적록색맹의 구역 개수

for i in range(N):
    for j in range(N):
        if not normal_visited[i][j]:
            normal(i, j, colors[i][j])
            n_cnt += 1
        if not rc_visited[i][j]:
            rg_color_blind(i, j, colors[i][j])
            rg_cnt += 1

print("{} {}".format(n_cnt, rg_cnt))
