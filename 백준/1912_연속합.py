# 백준 1912_연속합

import sys


n = int(sys.stdin.readline().strip())  # 정수의 개수
sequence = list(map(int, sys.stdin.readline().split()))  # 수열
dp = list(sequence)

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1] + sequence[i])

print(max(dp))
