# 백준 1309_동물원

import sys


N = int(sys.stdin.readline().strip())  # 우리의 크기
dp = [[0] * 3 for _ in range(N+1)]

# 시작지점 경우의 수
for i in range(3):
    dp[1][i] = 1

# 시작지점 이후의 경우의 수
for i in range(2, N+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901  # 왼쪽
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901  # 오른쪽
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901  # 없는 경우

print(sum(dp[N]) % 9901)
