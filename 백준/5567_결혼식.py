# 백준 5567_결혼식

import sys


n = int(sys.stdin.readline().strip())  # 동기의 수
m = int(sys.stdin.readline().strip())  # 관계의 수
edge = [[] for _ in range(n+1)]  # 친구관계
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())  # a <-> b 친구관계
    edge[a].append(b)
    edge[b].append(a)

visited = [0] * (n+1)
for friend in edge[1]:
    visited[friend] = 1  # 친구

    for semi_friend in edge[friend]:
        visited[semi_friend] = 1  # 친구의 친구

visited[1] = 0  # 본인 제외
print(sum(visited))
