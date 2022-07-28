# 백준 1389 케빈 베이컨의 6단계 법칙

import sys
from collections import deque


def bfs(user):
    global minv, min_lst
    visited = [0] * (N+1)
    q = deque()
    q.append(user)
    visited[user] = 1

    while q:
        now = q.popleft()

        for i in range(1, N+1):
            if connect[now][i] and not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)

    sumv = sum(visited) - N  # 케빈 베이컨의 수

    if sumv < minv:
        minv = sumv
        min_lst = [user]

    elif sumv == minv:
        min_lst.append(user)


N, M = map(int, input().split())  # N: 유저의 수, M: 친구 관계의 수
connect = [[0] * (N+1) for _ in range(N+1)]  # 연결된 상태

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())  # 이어진 관계
    connect[A][B] = 1  # 양방향
    connect[B][A] = 1

min_lst = []  # 최소 관계 리스트
minv = 99999999  # 최소 관계 수

for i in range(1, N+1):
    bfs(i)

min_lst.sort()  # 가장 작은 번호

print(min_lst[0])
