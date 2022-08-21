# 백준 1916_최소비용 구하기

import sys
import heapq


def dijkstra(start, end):
    cost = [INF] * (N+1)  # 비용
    heap = []
    heapq.heappush(heap, [0, start])
    cost[start] = 0  # 시작지점은 비용없음

    while heap:
        distance, now = heapq.heappop(heap)  # 오는데 드는 비용, 현재 위치

        if cost[now] < distance:
            continue

        for new_distance, new in connect[now]:  # 최소 비용 찾기
            temp_cost = cost[now] + new_distance

            if cost[new] > temp_cost:
                cost[new] = temp_cost
                heapq.heappush(heap, [temp_cost, new])

    return cost[end]


N = int(sys.stdin.readline().strip())  # N: 도시의 개수
M = int(sys.stdin.readline().strip())  # M: 버스의 개수
connect = [[] for _ in range(N+1)]  # 연결된 도시 (비용, 목적지)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())  # a -> b, c: 비용
    connect[a].append([c, b])

s, e = map(int, sys.stdin.readline().split())  # 시작지점, 도착지점
INF = int(1e8)  # 최대 길이

print(dijkstra(s, e))
