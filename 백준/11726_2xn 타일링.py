# 백준 11726_2xn 타일링


n = int(input())  # n: 2*n
dp = [0] * (n+1)
dp[1:3] = [1, 2]

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
