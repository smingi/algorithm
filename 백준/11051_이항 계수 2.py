# 백준 11051_이항 계수 2

import sys


N, K = map(int, sys.stdin.readline().split())  # N: 자연수, K: 정수
dp = [1, 1] + [0] * (N-1)

for i in range(2, N+1):
    dp[i] = dp[i-1] * i

print((dp[N] // (dp[K] * dp[N-K])) % 10007)
