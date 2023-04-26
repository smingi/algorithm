# 백준 15656_N과 M (7)

import sys
from itertools import product


N, M = map(int, sys.stdin.readline().split())  # N: 자연수의 갯수, M: 길이
numbers = sorted(list(map(int, sys.stdin.readline().split())))  # 자연수

for pro in product(numbers, repeat=M):
    print(*pro)
