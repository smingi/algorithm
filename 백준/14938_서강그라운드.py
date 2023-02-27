# 백준 14938_서강그라운드

import sys
import heapq


def dijkstra(start):
    heap = []
    visited = [INF] * (n+1)
    heapq.heappush(heap, [0, start])
    visited[start] = 0

    while heap:
        now_distance, now = heapq.heappop(heap)

        if visited[now] < now_distance or now_distance > m:  # 백트래킹
            continue

        for new_distance, new in road[now]:
            distance = new_distance + now_distance
            if visited[new] > distance and distance <= m:
                visited[new] = distance
                heapq.heappush(heap, [distance, new])

    item = 0  # 탐색후 아이템 개수 구하기
    for i in range(1, n+1):
        if visited[i] != INF:
            item += items[i]

    return item


n, m, r = map(int, input().split())  # n: 지역의 개수, m: 수색 범위, r: 길의 개수
items = list(map(int, input().split()))  # 지역별 아이템 개수
items.insert(0, 0)  # 번호와 인덱스가 일치하도록 앞에 0을 추가
road = [[] for _ in range(n+1)]  # 이어진 길

for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())  # a <-> b, c: 길이
    road[a].append([c, b])
    road[b].append([c, a])  # 양방향

INF = int(1e9)
max_item = 0  # 가장 많은 아이템 개수
for i in range(1, n+1):  # 가장 많은 아이템 개수 구하기
    max_item = max(max_item, dijkstra(i))

print(max_item)  # 가장 많은 아이템 개수 출력
