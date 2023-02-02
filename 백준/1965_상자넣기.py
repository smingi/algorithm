# 백준 1965_상자넣기

import sys


n = int(sys.stdin.readline().strip())  # 상자의 개수
box = list(map(int, sys.stdin.readline().split()))  # 상자의 크기
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
