# 백준 2003_수들의 합 2

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 수열의 길이, M: 합
numbers = list(map(int, sys.stdin.readline().split()))

s, e, cnt = 0, 1, 0
while s <= e <= N:
    now = sum(numbers[s:e])

    if now == M:
        cnt += 1
        e += 1

    elif now < M:
        e += 1

    else:
        s += 1

print(cnt)
