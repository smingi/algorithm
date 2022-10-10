# 백준 11779_최소 비용 구하기

import sys
import heapq


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, [0, start])
    cost[start] = 0

    while heap:
        now_cost, now = heapq.heappop(heap)  # 사용한 비용, 현재 위치

        if cost[now] < now_cost:  # 백트래킹
            continue

        for new_cost, new in bus[now]:
            temp_cost = now_cost + new_cost  # 새로운 경로로 가는 비용
            if cost[new] > temp_cost:
                cost[new] = temp_cost
                root[new] = now  # 가까운 경로 저장
                heapq.heappush(heap, [temp_cost, new])

    return cost[end]


n = int(sys.stdin.readline().strip())  # 도시의 개수
m = int(sys.stdin.readline().strip())  # 버스의 개수
bus = [[] for _ in range(n+1)]  # 목적지로 가는 버스(비용, 목적지)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())  # a -> b, c: 비용
    bus[a].append([c, b])

s, e = map(int, sys.stdin.readline().split())  # s: 시작지점, e: 도착지점
INF = int(1e9)  # 최대 비용
cost = [INF for _ in range(n+1)]  # 최소 비용
root = [s for _ in range(n+1)]  # 가까운 경로 찾기

print(dijkstra(s, e))  # 최소 비용 출력

path = [e]  # 지나온 경로
index = e  # 도착지부터 시작점 순으로 탐색

while index != s:
    path.append(root[index])
    index = root[index]

path.reverse()  # 시작점부터 시작하도록 변경

print(len(path))  # 경로 개수 출력
for p in path:  # 지나온 경로 출력
    print(p, end=" ")
