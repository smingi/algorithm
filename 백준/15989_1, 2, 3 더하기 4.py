# 백준 15989_1, 2, 3 더하기 4

import sys


dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    n = int(sys.stdin.readline().strip())  # 정수
    print(dp[n])
