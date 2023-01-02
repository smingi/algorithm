# 백준 1717_집합의 표현

import sys
sys.setrecursionlimit(10**6)


def find_parent(x):  # 부모노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union(a, b):
    p_a = find_parent(a)
    p_b = find_parent(b)

    parent[p_a] = p_b


n, m = map(int, sys.stdin.readline().split())  # n+1개의 집합, 연산의 개수
parent = [i for i in range(n+1)]  # 부모노드
for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())  # 명령, a, b

    # 연결하기
    if command == 0:
        if find_parent(a) != find_parent(b):
            union(a, b)

    # 비교하기
    if command == 1:
        # 다른 집합인 경우
        if find_parent(a) != find_parent(b):
            print("NO")

        # 같은 집합인 경우
        else:
            print("YES")
