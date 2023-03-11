# 백준 14235_크리스마스 선물

import sys
import heapq


n = int(sys.stdin.readline().strip())  # 방문한 횟수
q = []
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))

    if lst[0] == 0:
        if q:
            print(-heapq.heappop(q))

        else:
            print(-1)

    else:
        for i in range(1, len(lst)):
            heapq.heappush(q, -lst[i])
