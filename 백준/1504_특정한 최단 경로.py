# 백준 1504_특정한 최단 경로

import sys
import heapq


def dijkstra(start, end):
    visited = [INF] * (N+1)  # 경로 길이
    heap = []
    heapq.heappush(heap, [0, start])
    visited[start] = 0  # 시작지점은 0

    while heap:
        distance, now = heapq.heappop(heap)  # 오는데 걸린 거리, 현재 위치

        for new_distance, new in edge[now]:  # 최단 거리 찾기
            if visited[new] > visited[now] + new_distance:
                visited[new] = visited[now] + new_distance
                heapq.heappush(heap, [visited[now] + new_distance, new])

    return visited[end]


N, E = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수
edge = [[] for _ in range(N+1)]  # 연결된 간선 (거리, 목적지)

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())  # a <-> b, c: 거리
    edge[a].append([c, b])
    edge[b].append([c, a])  # 양방향

v1, v2 = map(int, sys.stdin.readline().split())  # 꼭 거쳐야하는 정점
INF = int(1e9)  # 최대 길이

# 1번에서 v1, v2를 거쳐 N으로 가는 방법
a = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)  # 1 -> v1 -> v2 -> N
b = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)  # 1 -> v2 -> v1 -> N

if a >= INF and b >= INF:  # 최단 경로가 없는 경우
    print(-1)
else:
    print(min(a, b))  # 최단 경로 출력
