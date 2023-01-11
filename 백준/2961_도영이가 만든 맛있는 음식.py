# 백준 2961_도영이가 만든 맛있는 음식

import sys
from itertools import combinations


N = int(sys.stdin.readline().strip())  # 재료의 개수
favor = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 신맛(곱), 쓴맛(합)
min_diff = int(1e9)  # 최소 차이

for i in range(1, N+1):
    for combination in combinations(favor, i):
        sour, bitter = 1, 0

        for s, b in combination:
            sour *= s  # 신맛(곱)
            bitter += b  # 쓴맛(합)

        min_diff = min(min_diff, abs(sour - bitter))

print(min_diff)
