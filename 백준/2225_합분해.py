# 백준 2225_합분해

import sys


N, K = map(int, sys.stdin.readline().split())  # N: 합이 되는 수, K: 더하는 정수의 개수
res = 1000000000  # 나머지를 구할 수
dp = [[0] * (N+1) for _ in range(K+1)]

# 숫자를 1개만 사용하는 경우
for value in range(1, N+1):
    dp[1][value] = 1

# 숫자를 2개이상 사용하는 경우
for cnt in range(2, K+1):
    dp[cnt][0] = 1

    for value in range(1, N+1):
        dp[cnt][value] = (dp[cnt-1][value] + dp[cnt][value-1]) % res

print(dp[K][N])
