# 백준 2479_경로 찾기

import sys
from collections import deque


def check(a, b):  # 해밍거리 체크
    distance = 0

    for i in range(K):
        if code[a][i] != code[b][i]:
            distance += 1

            if distance > 1:
                return False

    if distance == 1:
        return True

    return False


def bfs():
    q = deque()
    visited = [0] * (N+1)
    q.append([start, [start]])
    visited[start] = 1

    while q:
        pre, lst = q.popleft()  # 이전 경로, 지나온 경로

        if pre == end:
            return " ".join(map(str, lst))

        for i in range(1, N+1):
            if not visited[i] and check(pre, i):
                q.append([i, lst + [i]])
                visited[i] = 1

    return -1


N, K = map(int, sys.stdin.readline().split())  # N: 이진 코드의 개수, K: 이진 코드의 길이
code = ["0"] + [sys.stdin.readline().strip() for _ in range(N)]  # 이진코드
start, end = map(int, sys.stdin.readline().split())  # 시작지점, 도착지점

print(bfs())
