# 백준 13301_타일 장식물

import sys


N = int(sys.stdin.readline().strip())  # N개의 타일
dp = [0] * (N+2)
dp[1] = 1

for i in range(2, N+2):
    dp[i] = dp[i-1] + dp[i-2]

print((dp[N] + dp[N+1]) * 2)
