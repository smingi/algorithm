# 백준 2294_동전 2

import sys


n, k = map(int, sys.stdin.readline().split())  # n: 동전의 종류, k: 원하는 가치
coin = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 동전
dp = [10001] * (k+1)
dp[0] = 0

for c in coin:
    for value in range(c, k+1):
        dp[value] = min(dp[value], dp[value-c] + 1)

if dp[k] == 10001:
    print(-1)

else:
    print(dp[k])
