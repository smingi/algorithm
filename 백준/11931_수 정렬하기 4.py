# 백준 11931_수 정렬하기 4

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 수의 개수
q = []
for _ in range(N):
    number = int(sys.stdin.readline().strip())  # 숫자
    heapq.heappush(q, -number)

while q:
    print(-heapq.heappop(q))
