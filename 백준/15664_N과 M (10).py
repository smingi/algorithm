# 백준 15664_N과 M (10)

import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())  # N: 자연수의 개수, M: 길이
A = sorted(list(map(int, sys.stdin.readline().split())))  # 수열

for com in sorted(set(combinations(A, M))):
    print(*com)
