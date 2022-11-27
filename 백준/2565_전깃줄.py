# 백준 2565_전깃줄

import sys


n = int(sys.stdin.readline().strip())  # 전깃줄의 갯수
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 연결된 전선(A <-> B)
lines.sort()  # 왼쪽 전봇대 기준으로 순서대로 주어지도록 정렬
dp = [1] * (n+1)

# 오른쪽 전봇대 기준으로 증가하는 수열의 길이 찾기
for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 적게 없애는 전깃줄의 개수(전깃줄의 개수에서 가장 긴 증가하는 수열의 길이를 뺀 수)
print(n - max(dp))
