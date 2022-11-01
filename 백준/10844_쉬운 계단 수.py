# 백준 10844_쉬운 계단 수

import sys


N = int(sys.stdin.readline().strip())  # 길이
dp = [[0] * 10 for _ in range(N+1)]

# 한자리인 경우
for i in range(1, 10):
    dp[1][i] = 1

# 두자리 이상인 경우
for i in range(2, N+1):
    for j in range(10):
        if j == 0:  # 왼쪽
            dp[i][j] = dp[i-1][1]

        elif j == 9:  # 오른쪽
            dp[i][j] = dp[i-1][8]

        else:  # 중간
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
