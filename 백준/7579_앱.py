# 백준 7579_앱

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 실행중인 앱, M: 새로운 앱을 위해 필요한 메모리 바이트
Am = [0] + list(map(int, sys.stdin.readline().split()))  # 사용중인 메모리 바이트
C = [0] + list(map(int, sys.stdin.readline().split()))  # 비활성화 비용
min_cost = sum(C)  # 최소 비용
dp = [[0 for _ in range(min_cost + 1)] for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(len(dp[0])):
        if C[i] > j:  # 비용이 j보다 큰 경우
            dp[i][j] = dp[i-1][j]

        else:  # 비용이 j보다 작은 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-C[i]] + Am[i])

        if dp[i][j] >= M:  # 원하는 용량을 확보한 경우
            min_cost = min(min_cost, j)

print(min_cost)
