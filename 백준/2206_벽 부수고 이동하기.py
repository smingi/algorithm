# 백준 2206_벽 부수고 이동하기

import sys
from collections import deque


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        r, c, block = q.popleft()  # r: 행, c: 열, block: 벽을 넘었는지 여부

        if r == N-1 and c == M-1:  # 목적지 도착
            return visited[r][c][block]

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc][block]:  # 범위 내에 처음 방문한 경우
                if board[nr][nc] == 0:  # 벽이 없는 경우
                    visited[nr][nc][block] = visited[r][c][block] + 1
                    q.append([nr, nc, block])
                elif board[nr][nc] == 1 and not block:  # 벽이 있고 넘은 적이 없는 경우
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    q.append([nr, nc, block + 1])

    return -1


N, M = map(int, input().split())  # N: 새로, M: 가로
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]  # 지도

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]  # 방문여부 [벽 안 넘은 경로, 벽 넘은 경로]

result = bfs()  # 너비 우선 탐색 결과

print(result)
