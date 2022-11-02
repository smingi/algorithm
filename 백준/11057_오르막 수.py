# 백준 11057_오르막 수

import sys


N = int(sys.stdin.readline().strip())  # 길이
dp = [[0] * 10 for _ in range(N+1)]

# 1자리인 경우
for i in range(10):
    dp[1][i] = 1

# 2자리 이상인 경우
for i in range(2, N+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[N]) % 10007)
