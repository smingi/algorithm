# 백준 11066_파일 합치기(pypy3 사용)

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    K = int(sys.stdin.readline().strip())  # 장의 수
    cost = list(map(int, sys.stdin.readline().split()))  # 합치는 비용
    dp = [[0] * K for _ in range(K)]

    for i in range(K-1):
        dp[i][i+1] = cost[i] + cost[i+1]  # i부터 i+1 번째까지 파일 합치는 비용

        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + cost[j]  # i부터 i+j 번째까지 파일 합치는 비용

    for cnt in range(2, K):  # 합치는 개수
        for start in range(K-cnt):  # 시작지점
            end = start + cnt  # 도착지점

            # start 에서 end 까지의 최소비용 저장
            dp[start][end] += min(dp[start][x] + dp[x+1][end] for x in range(start, end))

    # 0부터 K-1까지 합치는 최소 비용 출력
    print(dp[0][K-1])
