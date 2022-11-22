# 백준 11722_가장 긴 감소하는 부분 수열

import sys


N = int(sys.stdin.readline().strip())  # 수열의 크기
sequence = [0] + list(map(int, sys.stdin.readline().split()))  # 수열
dp = [1] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if sequence[i] < sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
