# 백준 13335_트럭

import sys
from collections import deque


n, w, L = map(int, sys.stdin.readline().split())  # n: 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
truck = list(map(int, sys.stdin.readline().split()))  # 트럭의 무게
q = deque([0] * w)
idx = 0
result = 0

while True:
    # 걸린 시간
    result += 1

    # 나온 차량
    q.popleft()

    # 트럭 진입
    if idx < n:

        # 진입 가능
        if sum(q) + truck[idx] <= L:
            q.append(truck[idx])
            idx += 1

        # 진입 불가
        else:
            q.append(0)

    # 시뮬레이션 종료
    if idx >= n and not q:
        break

print(result)
