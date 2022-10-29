# 백준 11055_가장 큰 증가 부분 수열

import sys


N = int(sys.stdin.readline().strip())  # 수열의 크기
A = list(map(int, sys.stdin.readline().split()))  # 수열
dp = list(A)

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:  # 증가하는 부분인 경우
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
