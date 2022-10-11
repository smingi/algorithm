# 백준 2252_줄 세우기

import sys
from collections import deque


def topology_sort():  # 위상정렬
    result = []  # 정렬 결과
    q = deque()

    # 시작지점 큐에 넣기
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()  # 현재 위치
        result.append(now)  # 현재 위치 저장

        for i in graph[now]:
            indegree[i] -= 1  # 진입차수 감소

            if indegree[i] == 0:  # 진입차수가 0이면 q에 넣기
                q.append(i)

    print(" ".join(map(str, result)))


N, M = map(int, sys.stdin.readline().split())  # N: 학생 수, M: 비교 횟수
indegree = [0] * (N+1)  # 진입차수
graph = [[] for _ in range(N+1)]  # 연결된 상태

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())  # a -> b
    graph[a].append(b)
    indegree[b] += 1  # 진입차수 증가

topology_sort()
