# 백준 11659_구간 합 구하기4

import sys

N, M = map(int, input().split())  # N: 수의 개수 , M: 합을 구해야 하는 횟수
n_lst = list(map(int, input().split()))  # 수의 종류

dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + n_lst[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i-1])
