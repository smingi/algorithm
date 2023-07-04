# 백준 9657_돌 게임 3

import sys


N = int(sys.stdin.readline().strip())  # 돌의 개수
dp = [0] * (N+1)
dp[1:5] = [1, 0, 1, 1]

for i in range(5, N+1):
    if dp[i-1] + dp[i-3] + dp[i-4] == 3:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N]:
    print('SK')

else:
    print("CY")
