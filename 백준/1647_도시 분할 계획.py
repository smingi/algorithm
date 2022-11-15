# 백준 1647_도시 분할 계획

import sys


def find_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(a, b):  # 부모노드 통합
    p_a = find_parent(a)
    p_b = find_parent(b)

    if p_a < p_b:
        parent[p_b] = p_a

    else:
        parent[p_a] = p_b


N, M = map(int, sys.stdin.readline().split())  # N: 집의 개수, M: 길의 개수
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  # 연결된 길(a <-> b, c: 비용)
edge.sort(key=lambda x: x[2])  # 비용 적은 순으로 정렬
parent = [i for i in range(N+1)]  # 부모노드

connected = []  # 연결비용
for a, b, c in edge:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        connected.append(c)

print(sum(connected[0:-1]))
