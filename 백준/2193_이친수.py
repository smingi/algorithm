# 백준 2193_이친수

import sys


N = int(sys.stdin.readline().strip())  # 자리수
dp = [[0, 0] for _ in range(N+1)]
dp[1][1] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N]))
