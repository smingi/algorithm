# 백준 9566_돌 게임

import sys


N = int(sys.stdin.readline().strip())  # 돌 개수
dp = [0, 0, 1, 0] + [0] * (N-3)  # 상근 0, 창영 1

for i in range(4, N+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0

    else:
        dp[i] = 1

if dp[N]:
    print("CY")

else:
    print("SK")
