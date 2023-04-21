# 백준 15651_N과 M (3)

import sys
from itertools import product


N, M = map(int, sys.stdin.readline().split())  # N: 1 ~ N, M: 길이
numbers = [i for i in range(1, N+1)]

for pro in product(numbers, repeat=M):
    print(*pro)
