# 백준 2579_계단 오르기

import sys


N = int(input())  # 계단의 개수
scores = [int(sys.stdin.readline()) for _ in range(N)]  # 계단별 점수

dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = scores[i]
    elif i == 1:
        dp[i] = scores[i] + scores[i-1]
    elif i == 2:
        dp[i] = max(scores[i] + scores[i-2], scores[i] + scores[i-1])
    else:
        dp[i] = max(scores[i] + dp[i-2], scores[i] + scores[i-1] + dp[i-3])

print(dp[N-1])
