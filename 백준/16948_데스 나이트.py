# 백준 16948_데스 나이트

import sys
from collections import deque


def bfs():
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append([sr, sc])
    visited[sr][sc] = 1

    while q:
        r, c = q.popleft()

        if r == er and c == ec:
            return visited[r][c] - 1

        for new_r, new_c in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
            if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c]:
                q.append([new_r, new_c])
                visited[new_r][new_c] = visited[r][c] + 1

    return -1


N = int(sys.stdin.readline().strip())  # N * N
sr, sc, er, ec = map(int, sys.stdin.readline().split())  # 출발지 / 도착지
print(bfs())
