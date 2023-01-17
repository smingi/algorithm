# 백준 1939_중량제한

import sys


def find_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):  # 연결하기
    p_a = find_parent(a)
    p_b = find_parent(b)

    parent[p_a] = p_b


N, M = map(int, sys.stdin.readline().split())  # N: 섬의 개수, M: 다리의 개수
# 연결된 다리 정보(A <-> B, C: 중량제한)
edge = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
edge.sort(key=lambda x: -x[2])  # 중량제한이 높은 순으로 정렬
start, end = map(int, sys.stdin.readline().split())  # 연결해야 되는 섬의 번호
parent = [i for i in range(N+1)]  # 부모노드

for a, b, c in edge:
    union(a, b)

    # 시작지점과 도착지점이 연결되면 종료(중량제한이 내림차순이기 때문에 현재 중량이 최대중량)
    if find_parent(start) == find_parent(end):
        print(c)
        break
