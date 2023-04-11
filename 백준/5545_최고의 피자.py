# 백준 5545_최고의 피자

import sys


N = int(sys.stdin.readline().strip())  # 토핑의 종류
A, B = map(int, sys.stdin.readline().split())  # A: 도우의 가격, B: 토핑의 가격
dough = int(sys.stdin.readline().strip())  # 도우의 칼로리
cal = sorted([int(sys.stdin.readline().strip()) for _ in range(N)], reverse=True)  # 칼로리
total_cal = dough
price = A
result = int(total_cal / price)

for i in range(N):
    total_cal += cal[i]
    price += B
    result = max(result, int(total_cal / price))

print(result)
