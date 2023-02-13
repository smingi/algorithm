# 백준 2502_떡 먹는 호랑이

import sys


def find_A_B():
    for i in range(1, K):
        for j in range(1, K):
            dp = [0] * (D + 1)
            dp[1] = i
            dp[2] = j

            for m in range(3, D + 1):
                dp[m] = dp[m - 1] + dp[m - 2]

            if dp[D] == K:
                print(i)
                print(j)
                return


D, K = map(int, sys.stdin.readline().split())  # D: 넘어온 날, K: 준 떡의 개수
find_A_B()  # A, B 찾기
