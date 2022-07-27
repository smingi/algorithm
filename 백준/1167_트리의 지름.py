# 백준 1167_트리의 지름

import sys
from collections import deque


def bfs(idx):
    node, maxv = idx, 0  # 가장 거리가 먼 노트와 거리
    visited = [0] * (V+1)
    q = deque()
    q.append([idx, 0])
    visited[idx] = 1

    while q:
        now, sumv = q.popleft()

        if sumv > maxv:
            node = now
            maxv = sumv

        for num, dis in connect[now]:
            if not visited[num]:
                visited[num] = 1
                q.append([num, sumv + dis])

    return [node, maxv]  # 가장 거리가 먼 노드와 거리 반환


V = int(input())  # V: 정점의 개수
connect = [[] for _ in range(V+1)]  # 연결된 상태

for i in range(V):
    info = list(map(int, sys.stdin.readline().split()))
    now = info[0]

    for j in range(1, len(info)-1, 2):
        connect[now].append([info[j], info[j+1]])

node, distance = bfs(1)  # 시작점에서 가장 먼 노드와 거리
node, distance = bfs(node)  # 시작점에서 가장 멀리있던 노드와 가장 먼 노드와 거리

print(distance)
