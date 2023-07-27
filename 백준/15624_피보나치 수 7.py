# 백준 15624_피보나치 수 7

import sys


n = int(sys.stdin.readline().strip())  # 0 또는 자연수
dp = [0] * (n+1)
dp[0:3] = [0, 1, 1]

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[n])
