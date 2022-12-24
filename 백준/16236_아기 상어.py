# 백준 16236_아기 상어


from collections import deque


def bfs():
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([shark_r, shark_c])
    visited[shark_r][shark_c] = 1
    temp_distance_lst = []  # 먹을수 있는 물고기 위치와 거리

    while q:
        pr, pc = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = pr + dr
            nc = pc + dc

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if sea[nr][nc] <= size:  # 이동할 수 있는 곳
                    q.append([nr, nc])
                    visited[nr][nc] = visited[pr][pc] + 1

                    if 0 < sea[nr][nc] < size:  # 먹을수 있는 물고기 위치
                        temp_distance_lst.append([nr, nc, visited[nr][nc]])

    return sorted(temp_distance_lst, key=lambda x: (x[2], x[0], x[1]))


N = int(input())  # N * N
sea = [list(map(int, input().split())) for _ in range(N)]  # 물고기, 상어 위치

shark_r, shark_c = 0, 0  # 상어 위치
size = 2  # 상어 크기
fish_cnt = 0  # 물고기 숫자

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_r = i
            shark_c = j
            sea[i][j] = 0
        elif sea[i][j]:
            fish_cnt += 1

eated = 0  # 먹은 숫자
time = 0  # 걸린 시간

while fish_cnt:
    distance_lst = bfs()  # 먹을 수 있는 물고기 리스트

    if not distance_lst:  # 먹을수 있는 물고기가 없는 경우
        break

    time += distance_lst[0][2]-1  # 이동 시간
    shark_r = distance_lst[0][0]  # 이동한 행
    shark_c = distance_lst[0][1]  # 이동한 열
    sea[shark_r][shark_c] = 0  # 물고기 지우기
    fish_cnt -= 1  # 물고기수 감소
    eated += 1  # 먹은 숫자 +1

    if eated == size:  # 상어 크기 증가
        size += 1
        eated = 0

print(time)
