# 백준 16194_카드 구매하기 2

import sys


N = int(sys.stdin.readline().strip())  # 카드의 개수
cards = [0] + list(map(int, sys.stdin.readline().split()))  # 카드 금액
INF = int(1e9)
dp = [0] + [INF] * N

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + cards[j])

print(dp[N])
