# 백준 2342_Dance Dance Revolution

import sys

# 0: 중심, 1: 위쪽, 2: 왼쪽, 3: 아래쪽, 4: 오른쪽
# 중앙 -> 다른 지점: 2, 다른 지점 -> 인접지점: 3, 반대지점: 4, 같은 지점: 1


def cost(now, new):  # 이동 비용
    # 같은 지점: 1
    if now == new:
        return 1

    # 중앙 -> 다른 지점: 2
    if now == 0:
        return 2

    # 반대지점: 4
    if abs(now - new) % 2 == 0:
        return 4

    # 다른 지점 -> 인접지점: 3
    return 3


order = list(map(int, sys.stdin.readline().split()))  # 주어진 순서(마지막은 0)
n = len(order) - 1  # 명령 개수
INF = int(1e9)
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0  # 시작지점(움직인 순서, 왼발, 오른발)
min_cost = INF  # 최소 비용

for i in range(1, n+1):
    move = order[i-1]  # 움직일 위치

    for left in range(5):
        for right in range(5):
            # 왼발 이동
            dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + cost(left, move))

            # 오른발 이동
            dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + cost(right, move))

for left in range(5):
    for right in range(5):
        min_cost = min(min_cost, dp[n][left][right])

print(min_cost)
