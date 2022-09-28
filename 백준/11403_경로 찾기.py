# 백준 11403_경로 찾기

from collections import deque


def connect(idx):
    visited = [0] * N
    q = deque()
    q.append(idx)

    while q:
        now = q.popleft()

        for i in path[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                result[idx][i] = 1


N = int(input())  # 정점의 개수
path = [[] for _ in range(N)]  # 연결된 통로
result = [[0] * N for _ in range(N)]  # 결과

for i in range(N):
    i_path = list(map(int, input().split()))  # 통로 상태

    for j in range(N):
        if i_path[j] == 1:
            path[i].append(j)


for i in range(N):  # 연결하기
    connect(i)

for i in range(N):
    for j in range(N):
        print(result[i][j], end=" ")
    print()
