# 백준 15655_N과 M (6)

import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())  # N: 자연수의 개수, M: 길이
numbers = sorted(list(map(int, sys.stdin.readline().split())))  # 수열

for com in combinations(numbers, M):
    print(*com)
