# 백준 11404_플로이드

import sys

n = int(input())  # n: 도시의 개수
m = int(input())  # m: 버스의 개수

INF = int(1e9)  # 최대 숫자
cost = [[INF] * (n+1) for _ in range(n+1)]  # 경로별 비용

# 시작지점과 도착지점이 같은 경우는 없음
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            cost[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())  # a -> b, c: 비용
    if cost[a][b] > c:  # 동일 경로 중 가장 적은 비용 선택
        cost[a][b] = c

# 플로이드(Floyd Warshall) 알고리즘
for k in range(1, n+1):  # 경유지
    for i in range(1, n+1):  # 출발지
        for j in range(1, n+1):  # 목적지
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == INF:
            print(0, end=" ")
        else:
            print(cost[i][j], end=" ")
    print()
