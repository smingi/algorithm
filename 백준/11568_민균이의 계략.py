# 백준 11568_민균이의 계략

import sys


N = int(sys.stdin.readline().strip())  # 카드의 수
numbers = list(map(int, sys.stdin.readline().split()))  # 숫자
dp = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
