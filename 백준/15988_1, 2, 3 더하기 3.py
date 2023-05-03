# 백준 15988_1, 2, 3 더하기 3

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
dp = dict()
dp[1] = 1
dp[2] = 2
dp[3] = 4
last = 3  # 계산이 완료된 마지막 값

for _ in range(T):
    number = int(sys.stdin.readline().strip())  # 주어진 숫자

    # 값을 찾은 경우
    if number in dp:
        print(dp[number])

    # 값을 못 찾은 경우
    else:
        for i in range(last+1, number+1):
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

        print(dp[number])

        # 마지막 값 갱신
        last = number
