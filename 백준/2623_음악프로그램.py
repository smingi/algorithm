# 백준 2623_음악프로그램

import sys
from collections import deque


def topological_sort():  # 위상정렬
    result = []  # 결과
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:  # 진입차수가 0인경우
            q.append(i)

    while q:
        now = q.popleft()  # 현재 위치
        result.append(now)

        for new in graph[now]:
            indegree[new] -= 1

            if indegree[new] == 0:
                q.append(new)

    if len(result) == N:  # 순서를 정하는게 가능한 경우
        for r in result:
            print(r)
    else:
        print(0)


N, M = map(int, sys.stdin.readline().split())  # N: 가수의 수, M: 보조의 PD수
indegree = [0] * (N+1)  # 진입차수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    order = list(map(int, sys.stdin.readline().split()))  # 1번: 보조 PD 번호, 1번 이후: 순서

    for a, b in zip(order[1:], order[2:]):  # a -> b 순서
        graph[a].append(b)
        indegree[b] += 1

topological_sort()
