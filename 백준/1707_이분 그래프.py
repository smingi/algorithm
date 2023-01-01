# 백준 1707_이분 그래프

import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()

        for new in edge[now]:
            if not visited[new]:
                q.append(new)
                visited[new] = -visited[now]

            elif visited[new] == visited[now]:
                return False

    return True


K = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())  # V: 정점의 개수, E: 간선의 개수
    edge = [[] for _ in range(V+1)]  # 연결된 노드
    visited = [False] * (V+1)

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())  # 두개의 정점
        edge[u].append(v)
        edge[v].append(u)

    valid = True
    for i in range(1, V+1):
        if not visited[i]:
            valid = bfs(i)  # 조건에 맞는지 확인

            if not valid:
                break

    if valid:
        print("YES")

    else:
        print("NO")
