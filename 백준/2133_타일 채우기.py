# 백준 2133_타일 채우기

import sys


N = int(sys.stdin.readline().strip())  # 3*N 크기의 벽
dp = [0] * (N+1)
dp[0] = 1

for i in range(2, N+1, 2):
    dp[i] = dp[i-2] * 3

    for j in range(0, i-2, 2):
        dp[i] += dp[j] * 2

print(dp[N])
