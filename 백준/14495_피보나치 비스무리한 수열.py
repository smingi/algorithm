# 백준 14495_피보나치 비스무리한 수열

import sys


n = int(sys.stdin.readline().strip())  # 자연수
dp = [0] * 117
dp[0:4] = [0, 1, 1, 1]

for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[n])
