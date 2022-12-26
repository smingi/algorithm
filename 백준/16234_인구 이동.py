# 백준 16234_인구 이동

import sys
from collections import deque


def bfs(r, c, group):
    q = deque()
    q.append([r, c])
    visited[r][c] = group
    group_value[group][0] += country[r][c]  # 그룹에 속한 나라의 총 인구수
    group_value[group][1] += 1  # 그룹에 속한 나라의 개수

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c]:
                population = abs(country[now_r][now_c] - country[new_r][new_c])  # 두 나라의 인구차이

                if L <= population <= R:
                    q.append([new_r, new_c])
                    visited[new_r][new_c] = group
                    group_value[group][0] += country[new_r][new_c]  # 그룹에 속한 나라의 총 인구수
                    group_value[group][1] += 1  # 그룹에 속한 나라의 개수


N, L, R = map(int, sys.stdin.readline().split())  # N*N 크기의 땅, L명 이상, R명 이하
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 나라별 인구수
cnt = 0  # 반복 횟수
total_country = N * N  # 총 국가 개수

while True:
    visited = [[0] * N for _ in range(N)]
    group_value = [[0, 0, 0] for _ in range(total_country+1)]  # 그룹별 총합, 개수, 총합 // 개수
    flag = 0  # 그룹 구분

    # 그룹 구분하기
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                flag += 1
                bfs(i, j, flag)

    # 연합하는 국가가 없는 경우 종료
    if flag == total_country:
        break

    cnt += 1

    # 그룹별 새로운 인구수
    for i in range(flag, 0, -1):
        group_value[i][2] = group_value[i][0] // group_value[i][1]

    # 그룹별 새로운 인구수 저장
    for i in range(N):
        for j in range(N):
            country[i][j] = group_value[visited[i][j]][2]

print(cnt)
