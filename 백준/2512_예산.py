# 백준 2512_예산

import sys


N = int(sys.stdin.readline().strip())  # 지방의 수
cost = list(map(int, sys.stdin.readline().split()))  # 요청한 예산
M = int(sys.stdin.readline().strip())  # 총 예산
s, e = 0, max(cost)
result = 0

while s <= e:
    mid = (s+e)//2
    now = 0

    for c in cost:
        if c > mid:
            now += mid
        else:
            now += c

    if now <= M:
        result = max(result, mid)
        s = mid + 1
    else:
        e = mid - 1

print(result)
