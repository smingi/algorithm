# 백준 11279_최대 힙

import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)
