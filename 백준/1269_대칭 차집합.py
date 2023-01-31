# 백준 1269_대칭 차집합

import sys


A_cnt, B_cnt = map(int, sys.stdin.readline().split())  # A, B 집합의 원소의 개수
A = set(map(int, sys.stdin.readline().split()))  # A 집합
B = set(map(int, sys.stdin.readline().split()))  # B 집합

# 차집합의 합
print(len(A - B) + len(B - A))
