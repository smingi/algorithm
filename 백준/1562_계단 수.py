# 백준 1562_계단 수

import sys


N = int(sys.stdin.readline().strip())  # 자연수(1 ~ 100)
mod = 1000000000  # 나머지를 구할 수
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N+1)]

# 한개만 고른 경우
for i in range(10):
    dp[1][i][1 << i] = 1

# 두개이상 고른 경우
for i in range(2, N+1):  # 선택한 숫자 개수
    for j in range(10):  # 선택한 숫자
        for k in range(1024):  # 비트마스킹
            if j == 0:  # 맨 왼쪽인 경우
                dp[i][j][(1 << j) | k] += dp[i - 1][j + 1][k]

            elif j == 9:  # 맨 오른쪽인 경우
                dp[i][j][(1 << j) | k] += dp[i - 1][j - 1][k]

            else:  # 중간지점인 경우
                dp[i][j][(1 << j) | k] += dp[i - 1][j - 1][k]
                dp[i][j][(1 << j) | k] += dp[i - 1][j + 1][k]

            # 나머지 연산후 저장
            dp[i][j][(1 << j) | k] %= mod

result = 0  # 결과
for i in range(1, 10):
    result += dp[N][i][1023]  # 결과값 더하기
    result %= mod  # 나머지 연산

print(result)
