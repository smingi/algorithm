# 백준 15665_N과 M (11)

import sys
from itertools import product


N, M = map(int, sys.stdin.readline().split())  # N: 자연수의 갯수, M: 길이
numbers = sorted(list(set(map(int, sys.stdin.readline().split()))))

for per in product(numbers, repeat=M):
    print(*per)
