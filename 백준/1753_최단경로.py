# 백준 1753_최단경로


import sys
import heapq


def dijkstra():
    heap = []  # 힙
    min_distance[K] = 0
    heapq.heappush(heap, [0, K])

    while heap:
        distance, now = heapq.heappop(heap)

        if min_distance[now] < distance:  # 가지치기
            continue

        for v, w in edge[now]:  # 짧은 거리 찾기
            if min_distance[v] > min_distance[now] + w:
                min_distance[v] = min_distance[now] + w
                heapq.heappush(heap, [min_distance[v], v])


V, E = map(int, input().split())  # V: 정점의 개수, E: 간선의 개수
K = int(input())  # 시작점의 번호
edge = [[] for _ in range(V+1)]  # (간선, 가중치)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())  # u -> v, w: 가중치 (방향그래프)
    edge[u].append([v, w])

min_distance = [999999999] * (V+1)  # 최단 거리
dijkstra()  # 다익스트라

for i in range(1, V+1):
    if min_distance[i] == 999999999:
        print("INF")
    else:
        print(min_distance[i])
