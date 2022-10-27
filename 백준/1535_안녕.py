# 백준 1535_안녕

import sys


N = int(sys.stdin.readline().strip())  # 사람수
L = [0] + list(map(int, sys.stdin.readline().split()))  # 잃는 채력
J = [0] + list(map(int, sys.stdin.readline().split()))  # 얻는 기쁨
dp = [[0] * 100 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 100):
        if L[i] > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])

print(dp[-1][-1])
