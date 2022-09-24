# 백준 11053_가장 긴 증가하는 부분 수열


N = int(input())  # N: 수열의 크기
A = list(map(int, input().split()))  # A: 수열

dp = [0] * N
dp[0] = 1  # 시작점은 항상 1

for i in range(1, N):
    max_cnt = 0  # 최대 길이
    for j in range(i):
        if A[j] < A[i] and max_cnt < dp[j]:
            max_cnt = dp[j]

    dp[i] = max_cnt + 1

print(max(dp))
