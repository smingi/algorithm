# 백준 15903_카드 합체 놀이

import sys
import heapq


n, m = map(int, sys.stdin.readline().split())  # n: 카드의 개수, m: 합치는 횟수
card = list(map(int, sys.stdin.readline().split()))  # 카드

q = []
for c in card:
    heapq.heappush(q, c)

for _ in range(m):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a + b)
    heapq.heappush(q, a + b)

print(sum(q))
