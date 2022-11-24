# 백준 1766_문제집

import sys
import heapq


def topological_sort():  # 위상정렬
    result = []
    q = []

    for i in range(1, N+1):
        if in_degree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        result.append(now)

        for new in post_work[now]:
            in_degree[new] -= 1

            if in_degree[new] == 0:
                heapq.heappush(q, new)

    for order in result:
        print(order, end=" ")


N, M = map(int, sys.stdin.readline().split())  # N: 문제의 수, M: 정보의 개수
in_degree = [0] * (N+1)  # 진입차수
post_work = [[] for _ in range(N+1)]  # 후행 작업

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())  # a -> b 순서
    post_work[a].append(b)
    in_degree[b] += 1

topological_sort()
