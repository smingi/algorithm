# 백준 2740_행렬 곱셈

import sys


N, M = map(int, sys.stdin.readline().split())  # N: A의 새로, M: A의 가로
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 행렬 A
M2, K = map(int, sys.stdin.readline().split())  # M2: B의 새로, K: B의 가로
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M2)]  # 행렬 B
result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        sum_v = 0

        for k in range(M):
            sum_v += A[i][k] * B[k][j]

        result[i][j] = sum_v

for r in result:
    print(*r)
