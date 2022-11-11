# 백준 1699_제곱수의 합

import sys


N = int(sys.stdin.readline().strip())  # 자연수
squared = [i*i for i in range(1, N+1)]  # 제곱수
dp = [0] * (N+1)

for i in range(1, N+1):
    tmp_lst = []  # 경우의 수

    for square in squared:
        if square > i:  # 제곱수가 i보다 커지면 종료
            break

        tmp_lst.append(dp[i-square])  # 경우의 수 저장

    dp[i] = min(tmp_lst) + 1  # 가장 최솟값을 저장

print(dp[N])
