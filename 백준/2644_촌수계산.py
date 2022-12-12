# 백준 2644_촌수계산

import sys
from collections import deque


def bfs(start):
    q = deque()
    visited = [0] * (n+1)
    q.append([start, 0])
    visited[start] = 1

    while q:
        now, cnt = q.popleft()

        if now == b:
            return cnt

        for new in edge[now]:
            if not visited[new]:
                q.append([new, cnt+1])
                visited[new] = 1

    return -1


n = int(sys.stdin.readline().strip())  # 전체 사람의 수
a, b = map(int, sys.stdin.readline().split())  # 촌수를 계산해야 하는 번호
m = int(sys.stdin.readline().strip())  # 부모 자식들 간의 관계의 개수
edge = [[] for _ in range(n+1)]  # 1촌 관계

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())  # x: 부모, y: 자식
    edge[x].append(y)
    edge[y].append(x)

print(bfs(a))
