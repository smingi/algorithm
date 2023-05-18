# 백준 1312_소수

import sys


A, B, N = map(int, sys.stdin.readline().split())  # A: 분자, B: 분모, C: 자릿수

for _ in range(N):
    A = (A % B) * 10

print(A//B)
