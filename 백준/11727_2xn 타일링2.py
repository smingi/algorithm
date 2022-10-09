# 백준 11727_2xn 타일링2


n = int(input())  # n: 가로의 길이

dp = [0] * 1000
dp[0:4] = [1, 3, 5, 11]

for i in range(4, n):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n-1] % 10007)
