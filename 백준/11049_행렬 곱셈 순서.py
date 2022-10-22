# 백준 11049_행렬 곱셈 순서(pypy3 사용)

import sys


N = int(sys.stdin.readline().strip())  # 행렬의 개수
size = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 각 행렬의 크기
dp = [[0] * N for _ in range(N)]

for cnt in range(1, N):  # 계산하는 행렬 개수
    for start in range(N-cnt):  # 시작지점
        end = start + cnt  # 도착지점
        dp[start][end] = 2 ** 31  # 최대 연산이 2**31 - 1과 같거나 작다

        for k in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end] + size[start][0] * size[k][1] * size[end][1])

print(dp[0][N-1])
