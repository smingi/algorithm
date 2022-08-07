# 백준 1967_트리의 지름

import sys
from collections import deque


def bfs(k, sumv):
    global max_node, max_length

    visited = [0] * (n+1)
    q = deque()
    q.append([k, sumv])
    visited[k] = 1

    while q:
        num, temp_sumv = q.popleft()

        if max_length < temp_sumv:
            max_length = temp_sumv
            max_node = num

        for nums, weight in node[num]:
            if not visited[nums]:
                visited[nums] = 1
                q.append([nums, temp_sumv + weight])


n = int(input())  # n: 노드의 개수
node = [[] for _ in range(n+1)]  # 연결된 노드
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())  # p: 부모 노드, c: 자식 노드, w: 가중치
    node[p].append([c, w])
    node[c].append([p, w])

max_node = 0  # 가장 멀리있는 노드
max_length = 0  # 트리의 지름

bfs(1, 0)  # 시작점에서 가장 멀리있는 노드 찾기
bfs(max_node, 0)  # 가장 멀리있던 노드에서 가장 멀리있는 노드 찾기

print(max_length)  # 트리의 지름
