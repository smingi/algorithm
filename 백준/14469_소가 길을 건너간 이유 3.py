# 백준 14469_소가 길을 건너간 이유 3

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 양의 정수
q = []
for _ in range(N):
    arrive, delay = map(int, sys.stdin.readline().split())  # 도착시간, 걸리는 시간
    heapq.heappush(q, [arrive, delay])

time = 0
while q:
    arrive, delay = heapq.heappop(q)

    if time >= arrive:
        time += delay

    else:
        time = arrive + delay

print(time)
