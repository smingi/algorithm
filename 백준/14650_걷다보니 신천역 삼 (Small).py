# 백준 14650_걷다보니 신천역 삼 (Small)

import sys


N = int(sys.stdin.readline().strip())  # 자릿수
dp = [0] * (N+1)
dp[0:3] = [0, 0, 2]

for i in range(3, N+1):
    dp[i] = dp[i-1]*3

print(dp[N])
