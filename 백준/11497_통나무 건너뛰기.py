# 백준 11497_통나무 건너뛰기

import sys


T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 통나무의 개수
    wood = list(map(int, sys.stdin.readline().split()))  # 나무
    wood.sort(reverse=True)
    result = 0

    for i in range(N-2):
        result = max(result, wood[i] - wood[i+2])

    print(result)
