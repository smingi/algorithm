# 백준 1149_RGB 거리

import sys


N = int(input())  # N: 집 수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 페인트하는 비용

for i in range(1, N):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])  # 앞집이 빨간색인 경우 (초록 or 파랑) 중 최소비용 선택
    cost[i][1] += min(cost[i - 1][0], cost[i - 1][2])  # 앞집이 초록색인 경우 (빨강 or 파랑) 중 최소비용 선택
    cost[i][2] += min(cost[i - 1][0], cost[i - 1][1])  # 앞집이 파란색인 경우 (빨강 or 초록) 중 최소비용 선택

print(min(cost[N-1]))  # 최소 비용
