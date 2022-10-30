# 백준 1446_지름길

import sys
import heapq


def dijkstra():
    q = []
    heapq.heappush(q, [0, 0])
    INF = int(1e9)
    dp = [INF] * (D+1)
    dp[0] = 0

    while q:
        now_distance, now = heapq.heappop(q)

        if dp[now] < now_distance:
            continue

        for new_distance, new in edge[now]:
            if new <= D and new_distance + now_distance < dp[new]:
                dp[new] = new_distance + now_distance
                heapq.heappush(q, [new_distance + now_distance, new])

    print(dp[D])


N, D = map(int, sys.stdin.readline().split())  # N: 지름길의 개수, D: 고속도로의 길이
edge = [[[1, i+1]] for i in range(D+1)]  # 연결된 길(거리, 목적지)

for _ in range(N):
    start, end, distance = map(int, sys.stdin.readline().split())

    if end <= D:
        edge[start].append([distance, end])

dijkstra()
