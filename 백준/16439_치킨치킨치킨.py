# 백준 16439_치킨치킨치킨

import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())  # N: 회원의 수, M: 치킨의 종류
preference = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 선호도
result = 0

for a, b, c in combinations([i for i in range(M)], 3):
    max_v = 0

    for i in range(N):
        max_v += max(preference[i][a], preference[i][b], preference[i][c])

    result = max(result, max_v)

print(result)
