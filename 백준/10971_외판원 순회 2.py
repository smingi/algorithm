# 백준 10971_외판원 순회 2

import sys


def dfs(now, sum_v):
    global result

    # 도착지점
    if sum(visited) == N:
        if cost[now][i]:
            result = min(result, sum_v + cost[now][i])
        return

    # 백트래킹
    if sum_v >= result:
        return

    for new in range(N):
        if not visited[new] and cost[now][new]:
            visited[new] = 1
            dfs(new, sum_v + cost[now][new])
            visited[new] = 0


N = int(sys.stdin.readline().strip())  # N: 도시의 수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 비용
visited = [0] * N
result = 1e9

for i in range(N):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(result)
