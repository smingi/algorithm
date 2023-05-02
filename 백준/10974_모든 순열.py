# 백준 10974_모든 순열

import sys
from itertools import permutations


N = int(sys.stdin.readline().strip())  # 1 ~ N
for per in permutations([i for i in range(1, N+1)], N):
    print(*per)
