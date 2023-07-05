# 백준 16562_친구비

import sys
import heapq


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


N, M, k = map(int, sys.stdin.readline().split())  # N: 학생 수, M: 친구관계 수, k: 가지고 있는 돈
cost = list(map(int, sys.stdin.readline().split()))  # 비용
q = []  # 연결할 친구 목록
parent = [i for i in range(N+1)]  # 부모노드

# 최소비용인 친구부터 연결
for i in range(N):
    heapq.heappush(q, [cost[i], i+1])

# 친구끼리 연결
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

result = 0
while k > 0 and q:
    cost, friend = heapq.heappop(q)

    # 연결할 수 없는 경우
    if cost > k:
        break

    # 연결할 친구가 있는 경우
    if find_parent(0) != find_parent(friend):
        result += cost
        k -= cost
        union(0, friend)

# 성공 여부
success = True
for i in range(1, N):
    if find_parent(0) != find_parent(i):
        success = False
        break

if success:
    print(result)

else:
    print("Oh no")
