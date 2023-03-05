# 백준 2660_회장뽑기

import sys


n = int(sys.stdin.readline().strip())   # 회원수
edge = [[51] * (n+1) for _ in range(n+1)]
while True:
    a, b = map(int, sys.stdin.readline().split())  # a와 b는 친구관계

    # 입력종료조건
    if a == -1 and b == -1:
        break

    edge[a][b] = 1
    edge[b][a] = 1

for i in range(1, n+1):
    edge[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if edge[i][j] != 0 and edge[i][j] != 1 and edge[i][j] > edge[i][k] + edge[k][j]:
                edge[i][j] = edge[i][k] + edge[k][j]

result = [51]
for i in range(1, n+1):
    result.append(max(edge[i][1:]))

minv = min(result)
print(minv, result.count(minv))
for i in range(1, n+1):
    if result[i] == minv:
        print(i, end=" ")
