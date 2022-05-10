# swea 14195 미생물 관찰


# dfs로 미생물 현황 파악
def run(r, c, pr, pc, target):
    global count
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr = pr + dr
        nc = pc + dc

        if 0 <= nr < r and 0 <= nc < c:
            if lst[nr][nc] == target and not visited[nr][nc]:
                visited[nr][nc] = 1
                count += 1
                run(r, c, nr, nc, target)


T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())
    lst = [list(input()) for _ in range(r)]
    visited = [[0] * c for _ in range(r)]
    result = []  # 미생물 현황 저장 [미생물 종류, 미생물 크기]

    for i in range(r):
        for j in range(c):
            if not visited[i][j]:
                count = 0
                run(r, c, i, j, lst[i][j])
                result.append([lst[i][j], count])

    a = 0
    b = 0
    maxv = 0
    for i in range(len(result)):
        if result[i][0] == 'A':
            a += 1
        elif result[i][0] == 'B':
            b += 1
        if result[i][1] > maxv:
            maxv = result[i][1]

    print('#{} {} {} {}'.format(tc, a, b, maxv))
