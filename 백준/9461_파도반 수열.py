# 백준 9461_파도반 수열


T = int(input())  # 테스트케이스

dp = [0] * 100
dp[0:3] = [1, 1, 1]
for i in range(3, 100):  # 미리 계산
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(T):
    N = int(input())  # N 번쨰 수를 찾아야 함

    print(dp[N-1])  # 원하는 부분 출력
