# 백준 8979_올림픽

import sys


N, K = map(int, sys.stdin.readline().split())  # N: 국가의 수, K: 등수를 알고 싶은 국가
medal = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)],
               key=lambda x: [-x[1], -x[2], -x[3]])  # 매달

idx = [medal[i][0] for i in range(N)].index(K)

for i in range(N):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break
