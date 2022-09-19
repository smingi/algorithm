# 백준 9465_스티커

import sys


T = int(input())  # 테스트케이스
for _ in range(T):
    n = int(sys.stdin.readline())  # n줄
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]  # 스티커 점수

    dp = [[0] * n for _ in range(2)]

    for j in range(n):  # 가로
        for i in range(2):  # 새로
            if j > 1:  # 세 번째 줄 이후
                dp[i][j] = max(dp[(i+1) % 2][j-1] + sticker[i][j], dp[(i+1) % 2][j-2] + sticker[i][j], dp[i][j-2] + sticker[i][j])
            elif j > 0:  # 두 번째 줄
                dp[i][j] = dp[(i+1) % 2][j-1] + sticker[i][j]
            else:  # 첫 번째 줄
                dp[i][j] = sticker[i][j]

    print(max(map(max, dp)))  # 가장 가치가 큰 경우 출력
