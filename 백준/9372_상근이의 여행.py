# 백준 9372_상근이의 여행

import sys


def dfs(now, cnt):
    visited[now] = 1

    for new in edge[now]:
        if not visited[new]:
            cnt = dfs(new, cnt+1)

    return cnt


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())  # N: 국가의 수, M: 비행기의 종류
    edge = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        edge[a].append(b)
        edge[b].append(a)

    print(dfs(1, 0))
