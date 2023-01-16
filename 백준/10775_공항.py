# 백준 10775_공항

import sys


def find_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):  # 연결하기
    p_a = find_parent(a)
    p_b = find_parent(b)

    parent[p_a] = p_b


G = int(sys.stdin.readline().strip())  # 게이트의 수
P = int(sys.stdin.readline().strip())  # 비행기의 수
parent = [i for i in range(G+1)]  # 부모노드
cnt = 0

for i in range(P):
    gi = int(sys.stdin.readline().strip())  # (1 ~ gi)의 게이트만 연결
    parent_gi = find_parent(gi)

    # 연결할 수 없으면 종료
    if parent_gi == 0:
        break

    # 연결
    union(parent_gi, parent_gi-1)
    cnt += 1

print(cnt)
