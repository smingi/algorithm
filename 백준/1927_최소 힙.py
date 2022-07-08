# 백준 1927_최소 힙

import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap):
            pop_number = heapq.heappop(heap)
            print(pop_number)
        else:
            print(0)
    else:
        heapq.heappush(heap, num)