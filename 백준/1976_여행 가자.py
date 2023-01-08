# 백준 1976_여행 가자

import sys


def find_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):  # 연결하기기
    p_a = find_parent(a)
    p_b = find_parent(b)

    if p_a > p_b:
        parent[p_a] = p_b

    else:
        parent[p_b] = p_a


N = int(sys.stdin.readline().strip())  # 도시의 수
M = int(sys.stdin.readline().strip())  # 여행 계획에 속한 도시들의 수
connect = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 연결된 도시들의 정보
travel = list(map(int, sys.stdin.readline().split()))  # 여행 계획에 속한 도시
parent = [i for i in range(N+1)]  # 부모노드

for i in range(1, N+1):
    for j in range(1, N+1):
        if connect[i-1][j-1] and find_parent(i) != find_parent(j):
            union(i, j)

result = "YES"
start = find_parent(travel[0])  # 시작지점

for i in range(1, M):
    if start != find_parent(travel[i]):
        result = "NO"
        break

print(result)
