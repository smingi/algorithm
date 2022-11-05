# 백준 2293_동전 1

import sys


n, k = map(int, sys.stdin.readline().split())  # n: 동전의 개수, k: 원하는 가치
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 동전의 종류
dp = [1] + [0] * k

for coin in coins:
    for value in range(coin, k+1):
        dp[value] += dp[value - coin]

print(dp[k])
