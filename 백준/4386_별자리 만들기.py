# 백준 4386_별자리 만들기

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


n = int(sys.stdin.readline().strip())  # 별의 개수
star = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]  # 별의 위치
parent = [i for i in range(n)]  # 부모노드
cost = []  # 연결비용

# 연결 비용 찾기
for i in range(n-1):
    for j in range(i+1, n):
        temp_cost = ((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2) ** 0.5
        cost.append([temp_cost, i, j])

cost.sort()  # 낮은 비용 순으로 정렬
min_cost = 0  # 최소 비용

# 선 열결하기
for c, a, b in cost:
    if find_parent(a) != find_parent(b):
        union(a, b)
        min_cost += c

print(min_cost)
