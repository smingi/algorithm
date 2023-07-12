# 백준 16928_뱀과 사다리 게임

import sys
from collections import deque


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        now = q.popleft()  # 현위치

        for i in range(1, 7):
            new = now + i  # 주사위로 이동한 위치

            if new > 100:  # 100을 넘어가면 안됨
                continue

            location = board[new]  # 실제 위치 (사다리 또는 뱀 또는 제자리)

            if not visited[location]:
                q.append(location)
                visited[location] = visited[now] + 1  # 주사위 횟수 추가

                if location == 100:  # 목적지에 도착하면 종료
                    return


N, M = map(int, input().split())  # N: 사다리 수, M: 뱀 수
board = [i for i in range(101)]  # 맵 상태

for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().split())  # x: 시작지점, y: 도착지점
    board[x] = y

visited = [0] * 101  # 방문 여부 + 주사위 횟수
bfs()
result = visited[100] - 1  # 처음 시작할 때 더해준 1을 빼줌

print(result)
