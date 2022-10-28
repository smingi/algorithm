# 백준 2156_포도주 시식


import sys


n = int(sys.stdin.readline().strip())  # 포도주 잔의 개수
glass = [0] + [int(sys.stdin.readline().strip()) for _ in range(n)]  # 포도주 잔
dp = [0] * (n+1)

if n == 1:
    print(glass[1])

elif n == 2:
    print(glass[1] + glass[2])

else:
    dp[1] = glass[1]
    dp[2] = glass[1] + glass[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + glass[i], dp[i-3] + glass[i-1] + glass[i])

    print(dp[n])
