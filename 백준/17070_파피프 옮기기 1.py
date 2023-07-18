# 백준 17070_파이프 옮기기 1


N = int(input())  # N: 집의 크기(N * N)
home = [list(map(int, input().split())) for _ in range(N)]  # 0: 빈칸, 1: 벽
home.insert(0, [0] * N)  # 인덱스 에러 방지
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N+1)]
dp[1][1] = [1, 0, 0]  # 시작지점(가로, 대각선, 새로로 오는 경로)

for i in range(1, N+1):
    for j in range(1, N):
        if i == 1 and j == 1:  # 시작지점
            continue

        if home[i][j] == 0:  # 빈칸인 경우
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]  # 가로로 오는 경로
            dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]  # 새로로 오는 경로

            if home[i-1][j] == 0 and home[i][j-1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])  # 대각선으로 오는 경로

print(sum(dp[N][N-1]))  # N, N에 도착하는 방법의 수
