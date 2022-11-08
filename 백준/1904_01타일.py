# 백준 1904_01타일

import sys


N = int(sys.stdin.readline().strip())  # 크기

if N == 1:
    print(1)

elif N == 2:
    print(2)

else:
    dp = [0] * (N + 1)
    dp[1:3] = [1, 2]

    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    print(dp[N])
