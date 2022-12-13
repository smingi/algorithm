# 백준 3190_뱀

import sys
from collections import deque


# 오른쪽 -> 아래 -> 왼쪽 -> 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def move():  # 뱀 이동
    q = deque()
    r, c = 0, 0  # 초기 위치
    q.append([r, c])
    board[r][c] = 2
    seconds = 1  # 걸린 시간
    idx = 0  # 방향

    while True:
        r, c = r + dr[idx], c + dc[idx]

        if 0 <= r < N and 0 <= c < N and board[r][c] != 2:

            # 사과가 없는 경우
            if not board[r][c]:
                tmp_r, tmp_c = q.popleft()
                board[tmp_r][tmp_c] = 0

            # 새로운 위치 이동
            board[r][c] = 2
            q.append([r, c])

            # 방향을 전환하는 경우
            if seconds in dic:

                # 왼쪽으로 이동하는 경우
                if dic[seconds] == "L":
                    idx = (idx + 3) % 4

                # 오른쪽으로 이동하는 경우
                else:
                    idx = (idx + 1) % 4

            seconds += 1

        else:  # 종료조건에 걸린 경우
            return seconds


N = int(sys.stdin.readline().strip())  # N*N 크기
board = [[0] * N for _ in range(N)]  # 보드
K = int(sys.stdin.readline().strip())  # 사과의 개수

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())  # 사과의 위치(행, 열)
    board[r-1][c-1] = 1

L = int(sys.stdin.readline().strip())  # 뱀의 방향 변환 횟수
dic = dict()

for _ in range(L):
    X, C = sys.stdin.readline().split()  # X초 뒤에 (L: 왼쪽, D: 오른쪽)으로 90도 회전
    dic[int(X)] = C

print(move())
