# 백준 11725 트리의 부모 찾기

from collections import deque


def find_p(x):  # 부모노드 찾는 함수
    visited = [0] * (N+1)  # 방문 체크
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for node in lst[x]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)
                p[node] = x


N = int(input())
p = [i for i in range(N+1)]  # 부모노드 리스트
lst = [[] for _ in range(N+1)]  # 인접 리스트

for _ in range(N-1):
    a, b = map(int, input().split())
    lst[b].append(a)
    lst[a].append(b)  # 양방향
find_p(1)  # 부모노드 찾기

for i in range(2, len(p)):
    print(p[i])
