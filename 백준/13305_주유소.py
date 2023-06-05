# 백준 13305_주유소

import sys


N = int(sys.stdin.readline().strip())  # 도시의 개수
distance = list(map(int, sys.stdin.readline().split()))  # 도로의 길이
cost = list(map(int, sys.stdin.readline().split()))  # 리터당 가격
min_cost = cost[0]
result = 0

for i in range(N-1):
    min_cost = min(min_cost, cost[i])
    result += (min_cost * distance[i])

print(result)
