# 백준 14501_퇴사

import sys


N = int(sys.stdin.readline().strip())  # 일수
plan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 일정
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + plan[i][0] > N:  # 기간내에 끝낼 수 없는 경우
        dp[i] = dp[i+1]

    else:  # 기간 내에 끝낼 수 있는 경우
        dp[i] = max(dp[i+1], dp[i + plan[i][0]] + plan[i][1])

print(dp[0])
