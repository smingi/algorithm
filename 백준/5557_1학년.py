# 백준 5557_1학년

import sys


N = int(sys.stdin.readline().strip())  # 숫자의 개수
numbers = list(map(int, sys.stdin.readline().split()))  # 숫자
dp = [[0] * 21 for _ in range(N-1)]

# 시작지점
dp[0][numbers[0]] = 1

for i in range(1, N-1):
    for j in range(21):  # 20을 넘는 수는 계산 x
        # 빼기
        if j - numbers[i] >= 0:
            dp[i][j-numbers[i]] += dp[i-1][j]

        # 더하기
        if j + numbers[i] < 21:
            dp[i][j+numbers[i]] += dp[i-1][j]

print(dp[N-2][numbers[N-1]])
