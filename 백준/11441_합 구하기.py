# 백준  11441_합 구하기

import sys


N = int(sys.stdin.readline().strip())  # 숫자의 개수
A = [0] + list(map(int, sys.stdin.readline().split()))  # 숫자
for i in range(1, N+1):
    A[i] += A[i-1]

M = int(sys.stdin.readline().strip())  # 구간의 개수
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())  # 구간
    print(A[j] - A[i-1])
