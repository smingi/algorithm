# 백준 7562_나이트의 이동

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    visited = [[0] * l for _ in range(l)]
    q.append([r, c, 0])
    visited[r][c] = 1

    while q:
        now_r, now_c, cnt = q.popleft()

        if now_r == end_r and now_c == end_c:
            return cnt

        for dr, dc in [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < l and 0 <= new_c < l and not visited[new_r][new_c]:
                q.append([new_r, new_c, cnt+1])
                visited[new_r][new_c] = 1


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    l = int(sys.stdin.readline().strip())  # l*l 크기
    start_r, start_c = map(int, sys.stdin.readline().split())  # 현재행, 현재열
    end_r, end_c = map(int, sys.stdin.readline().split())  # 목표행, 목표열

    print(bfs(start_r, start_c))
