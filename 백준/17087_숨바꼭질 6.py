# 백준 17087_숨바꼭질 6

import sys
import math


N, S = map(int, sys.stdin.readline().split())  # N: 동생의 수, S: 현 위치
A = list(map(int, sys.stdin.readline().split()))  # 동생들의 위치
gcd = abs(S - A[0])  # 최대 공약수

for i in range(1, N):
    gcd = math.gcd(abs(S - A[i]), gcd)

print(gcd)
