# 백준 15649_N과 M (1)

import sys
from itertools import permutations


N, M = map(int, sys.stdin.readline().split())  # 1~N, M: 길이

for per in permutations([i for i in range(1, N+1)], M):
    print(*per)
