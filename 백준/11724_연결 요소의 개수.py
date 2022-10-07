# 백준 11724 연결 요소의 개수

import sys
from collections import deque


def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = 1

    while q:
        now = q.popleft()

        for new in connect[now]:
            if not visited[new]:
                q.append(new)
                visited[new] = 1


N, M = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수
connect = [[] for _ in range(N+1)]  # 연결된 정점

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    connect[u].append(v)  # 양방향
    connect[v].append(u)

visited = [0] * (N+1)
cnt = 0  # 총 그룹 개수

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
