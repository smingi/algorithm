# 백준 2667_단지번호붙히기

def bfs(r, c, num):
    q = []
    q.append([r, c])
    lst[r][c] = num
    temp_cnt = 1
    while q:
        pr, pc = q.pop(0)
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] == 1:
                q.append([nr, nc])
                lst[nr][nc] = num
                temp_cnt += 1

    cnt_lst.append(temp_cnt)


N = int(input())
lst = [list(map(int, input())) for _ in range(N)]

cnt_lst = []
cnt = 1
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            cnt += 1
            bfs(i, j, cnt)

print(cnt-1)
cnt_lst.sort()
for i in range(len(cnt_lst)):
    print(cnt_lst[i])

