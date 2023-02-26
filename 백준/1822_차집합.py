# 백준 1822_차집합

import sys


a, b = map(int, sys.stdin.readline().split())  # A, B 집합 원소의 개수
A = set(map(int, sys.stdin.readline().split()))  # A 집합
B = set(map(int, sys.stdin.readline().split()))  # B 집합
result = list(A - B)
result.sort()

print(len(result))
if result:
    print(" ".join(map(str, result)))
