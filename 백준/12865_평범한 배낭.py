# 백준 12865 평범한 배낭

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N)]

for i in range(N):  # 물건 종류
    for j in range(1, K+1):  # 배낭 무게
        if j < lst[i][0]:  # 물건이 배낭 무게보다 무거우면
            dp[i][j] = dp[i-1][j]  # 넣기 전 상태 보전
        elif dp[i-1][j] > dp[i-1][j-lst[i][0]]+lst[i][1]:  # 같은 무게에서 새로 넣은 물건 가치보다 기존 가치가 클 때
            dp[i][j] = dp[i-1][j]  # 기존 물건 유지
        else:  # 같은 무게에서 새로 넣은 물건 가치가 클 때
            dp[i][j] = dp[i-1][j-lst[i][0]]+lst[i][1]  # 새로운 물건으로 교체


print(dp[N-1][K])  # 모든 물건을 넣고 무게가 k일 때 가장 큰 가치
