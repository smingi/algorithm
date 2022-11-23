# 백준 1922_네트워크 연결

import sys


def get_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = get_parent(parent[x])

    return parent[x]


def connect(a, b):  # 두개의 노드 연결하기
    p_a = get_parent(a)
    p_b = get_parent(b)

    if p_a < p_b:
        parent[p_b] = p_a

    else:
        parent[p_a] = p_b


N = int(sys.stdin.readline().strip())  # 컴퓨터의 수
M = int(sys.stdin.readline().strip())  # 연결할 수 있는 선의 수
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  # 연결할 수 있는 선(a<->b, 비용)
edge.sort(key=lambda x: x[2])  # 비용이 낮은 순으로 정렬
parent = [i for i in range(N+1)]  # 부모노드

min_cost = 0  # 최소비용
for a, b, c in edge:
    if get_parent(a) != get_parent(b):
        connect(a, b)
        min_cost += c

print(min_cost)
