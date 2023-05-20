# 백준 13699_점화식

import sys


n = int(sys.stdin.readline().strip())  # n 번째
dp = [0] * (n+1)
dp[0:4] = [1, 1, 2, 5]

for i in range(4, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[n])
