# 백준 1246_온라인 판매

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 달걀의 개수, M: 고객의 수
cost = sorted([int(sys.stdin.readline().strip()) for _ in range(M)])  # 비용
sum_v = 0  # 최대 값
price = 0  # 가격

for i in range(M):
    cnt = min(M-i, N)
    tmp_cost = cost[i] * cnt

    if sum_v < tmp_cost:
        sum_v = tmp_cost
        price = cost[i]

print(price, sum_v)
