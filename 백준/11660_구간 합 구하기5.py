# 11660_구간 합 구하기5

import sys


N, M = map(int, input().split())  # N: 표의 크기(N*N), M: 합을 구해야 하는 횟수
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 적혀있는 수

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):  # 적혀있는 수 + 왼쪽, 위쪽 값을 더한 후 중복으로 더한 왼쪽 위 값을 빼줌
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + lst[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # x2, y2의 값에서 범위에 포합되지 않는 왼쪽과 위쪽값을 빼준 후 중복으로 뺀 왼쪽 위 값을 더해줌
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
