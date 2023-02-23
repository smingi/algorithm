# 백준 2075_N번째 큰 수

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 줄의 수
heap = []

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))

    if not heap:
        for num in line:
            heapq.heappush(heap, num)

    else:
        for num in line:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
