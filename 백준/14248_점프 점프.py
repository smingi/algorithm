# 백준 14248_점프 점프

import sys
from collections import deque


def bfs():
    q = deque()
    visited = [0] * n
    q.append(s-1)
    visited[s-1] = 1

    while q:
        now = q.popleft()

        for new in [now+Ai[now], now-Ai[now]]:
            if 0 <= new < n and not visited[new]:
                q.append(new)
                visited[new] = 1

    return sum(visited)


n = int(sys.stdin.readline().strip())  # 돌의 개수
Ai = list(map(int, sys.stdin.readline().split()))  # 가능한 위치
s = int(sys.stdin.readline().strip())  # 출발지점
print(bfs())
