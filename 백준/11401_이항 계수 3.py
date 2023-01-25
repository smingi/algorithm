# 백준 11401_이항 계수 3

import sys


def square(a, b):  # a**b
    if b == 0:
        return 1

    divide = square(a, b//2)  # 분할 정복
    if b % 2:  # 홀수인 경우
        return (divide * divide * a) % mod

    else:  # 짝수인 경우
        return (divide * divide) % mod


N, K = map(int, sys.stdin.readline().split())  # N: 자연수, K: 정수
mod = 1000000007  # 나머지를 구할 수
dp = [1 for _ in range(N+1)]

for i in range(2, N+1):
    dp[i] = (dp[i-1] * i) % mod

numerator = dp[N]  # 분자
denominator = (dp[K] * dp[N-K]) % mod  # 분모

# 페르마의 소정리
print((numerator * square(denominator, mod-2)) % mod)
