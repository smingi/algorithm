# 백준 1197_최소 스패닝 트리

import sys


def find_p(a):  # 부모노드 찾기
    if a == parent[a]:
        return a

    else:
        parent[a] = find_p(parent[a])
        return parent[a]


def union(a, b):  # 결합
    a = find_p(a)
    b = find_p(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


V, E = map(int, input().split())  # V: 정점의 수, E: 간선의 개수
edge = []  # 간선
parent = [i for i in range(V+1)]  # 부모노드

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())  # A <-> B, C: 가중치
    edge.append([A, B, C])

edge.sort(key=lambda x: x[2])  # 가중치가 낮은 순으로 정렬
cnt = 1  # 시작지점 포함해서 1부터 시작
result = 0

while True:
    if cnt == V:  # 모든 정점이 연결되면 종료
        break

    a, b, c = edge.pop(0)

    if find_p(a) != find_p(b):  # 서로 연결이 되어있지 않은 경우
        union(a, b)  # 연결
        cnt += 1  # 개수 +1
        result += c  # 가중치 추가

print(result)
