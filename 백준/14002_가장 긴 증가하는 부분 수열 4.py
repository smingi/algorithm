# 백준 14002_가장 긴 증가하는 부분 수열 4

import sys


N = int(sys.stdin.readline().strip())  # 수열의 크기
A = list(map(int, sys.stdin.readline().split()))  # 수열
dp = [1] * N

# 가장 긴 증가하는 수열의 길이 찾기
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 수열의 순서 찾기
result = []  # 결과 순서(역순)
max_v = max(dp)  # 찾는 길이
for i in range(N-1, -1, -1):
    if dp[i] == max_v:
        result.append(A[i])
        max_v -= 1

# 수열의 길이 출력
print(len(result))

# 수열의 순서 출력
for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")
