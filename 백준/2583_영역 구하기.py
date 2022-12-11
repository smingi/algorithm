# 백준 2583_영역 구하기

import sys
from collections import deque


def bfs(r, c):
    q = deque()
    q.append([r, c])
    board[r][c] = 2
    cnt = 1

    while q:
        now_r, now_c = q.popleft()

        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_r = now_r + dr
            new_c = now_c + dc

            if 0 <= new_r < M and 0 <= new_c < N and board[new_r][new_c] == 0:
                q.append([new_r, new_c])
                board[new_r][new_c] = 2
                cnt += 1

    return cnt


M, N, K = map(int, sys.stdin.readline().split())  # M: 행, N: 열, K: 직사각형의 개수
board = [[0] * N for _ in range(M)]  # 모눈종이

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())  # 직사각형의 위치

    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

width = []  # 영역의 넓이

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            width.append(bfs(i, j))

width.sort()  # 오름차순으로 정렬

# 영역의 개수
print(len(width))

# 영역의 넓이
for w in width:
    print(w, end=" ")
