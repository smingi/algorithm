# 백준 11060_점프 점프

import sys


N = int(sys.stdin.readline().strip())  # 미로의 길이
maze = list(map(int, sys.stdin.readline().split()))  # 미로
dp = [1001 for _ in range(N)]
dp[0] = 0

for i in range(N):
    for j in range(i, i + maze[i] + 1):
        if j < N:
            dp[j] = min(dp[j], dp[i]+1)

if dp[N-1] == 1001:
    print(-1)

else:
    print(dp[N-1])
