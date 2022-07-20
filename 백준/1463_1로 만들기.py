# 백준 1463_1로 만들기


N = int(input())  # N: 1로 만들 정수
dp = [0] * (N+1)  # dp

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1  # 1을 뺴는 방법

    if i % 3 == 0 and i//3 > 0:  # 3으로 나누는 방법
        dp[i] = min(dp[i], dp[i//3]+1)

    if i % 2 == 0 and i//2 > 0:  # 2로 나누는 방법
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])
