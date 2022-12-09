# 백준 14003_가장 긴 증가하는 부분 수열 5

import sys
import bisect


N = int(sys.stdin.readline().strip())  # 수열의 크기
A = [0] + list(map(int, sys.stdin.readline().split()))  # 수열
dp = [0] * (N+1)
min_v = -int(1e10)  # 최솟값
lst = [min_v]

for i in range(1, N+1):
    if A[i] > lst[-1]:  # 수열의 값이 리스트 맨 뒤에 든 값보다 큰 경우
        lst.append(A[i])  # 리스트 맨 뒤에 수열의 값 넣기
        dp[i] = len(lst) - 1  # dp에 길이 저장

    else:  # 수열의 값이 리스트에 든 값보다 작은 경우
        dp[i] = bisect.bisect_left(lst, A[i])  # dp에 리스트에서 수열값의 왼쪽 인덱스 값 저장
        lst[dp[i]] = A[i]  # 리스트의 인덱스 위치에 수열 저장

# 결과 순서 찾기
max_v = max(dp) + 1  # 최대 길이 + 1
result = []  # 결과(역순)
for i in range(N, 0, -1):
    if dp[i] == max_v - 1:  # dp 길이의 값과 최대 길이가 같은 경우
        result.append(A[i])  # 결과에 수열의 값 넣기
        max_v = dp[i]  # 최대 길이 변경

print(len(result))  # 부분 수열의 길이
for i in range(len(result)-1, -1, -1):  # 부분 수열
    print(result[i], end=" ")
