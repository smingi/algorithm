# 백준 2887_행성 터널

import sys


def find_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):  # 연결하기
    p_a = find_parent(a)
    p_b = find_parent(b)

    if p_a > p_b:
        parent[p_a] = p_b

    else:
        parent[p_b] = p_a


N = int(sys.stdin.readline().strip())  # 행성의 개수
planet = [[i] + list(map(int, sys.stdin.readline().split())) for i in range(N)]  # 행성의 위치
distance = []  # 행성간의 거리 (행성1, 행성2, 거리)
parent = [i for i in range(N)]  # 부모노드

# 행성간의 거리 구하기
for j in range(1, 4):
    planet.sort(key=lambda x: x[j])  # 축별로 오름차순으로 정렬

    for i in range(1, N):
        distance.append([planet[i-1][0], planet[i][0],  abs(planet[i][j] - planet[i-1][j])])

# 비용이 낮은 순으로 정렬
distance.sort(key=lambda x: x[2])

result = 0
for a, b, cost in distance:
    if find_parent(a) != find_parent(b):
        result += cost
        union(a, b)

print(result)
