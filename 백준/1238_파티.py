# 백준 1238_파티

import sys
import heapq


def dijkstra(start, end):
    heap = []
    INF = int(1e9)  # 최대 시간
    distance = [INF] * (N+1)  # 걸리는 시간
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        time, now = heapq.heappop(heap)  # 오는데 걸린시간, 현재 위치

        if distance[now] < time:  # 백트래킹
            continue

        for new_time, new in road[now]:  # 갈 수 있는 곳에 걸리는 시간과 목적지
            if distance[now] + new_time < distance[new]:  # 최단 거리 찾기
                heapq.heappush(heap, [distance[now] + new_time, new])
                distance[new] = distance[now] + new_time

    return distance[end]


N, M, X = map(int, input().split())  # N: 학생의 수, M: 단방향 도로의 수, X: 피티가 열리는 마을

road = [[] for _ in range(N+1)]  # 도로 (걸리는 시간, 목적지)

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())  # a -> b, t: 시간
    road[a].append([t, b])

maxv = 0  # 가장 오래걸리는 시간

for i in range(1, N+1):
    time1 = dijkstra(i, X)  # 파티에 참석하러 가는 시간
    time2 = dijkstra(X, i)  # 파티에서 돌아오는 시간

    if time1 + time2 > maxv:  # 가장 오래걸리는 시간 찾기
        maxv = time1 + time2

print(maxv)
