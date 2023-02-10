# 백준 9625_BABBA

import sys


K = int(sys.stdin.readline().strip())  # 버튼을 누른 횟수
dp = [[0, 0] for _ in range(K+1)]
dp[0:2] = [[1, 0], [0, 1]]

for i in range(2, K+1):
    dp[i][0] = dp[i-1][1]  # A의 개수
    dp[i][1] = dp[i-1][0] + dp[i-1][1]  # B의 개수

print(dp[K][0], dp[K][1])
