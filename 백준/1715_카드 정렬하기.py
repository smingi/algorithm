# 백준 1715_카드 정렬하기

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 카드 묶음의 개수
q = []
for _ in range(N):
    card = int(sys.stdin.readline().strip())  # 카드 묶음
    heapq.heappush(q, card)

result = 0

# 가장 작은 2개를 합치기
for _ in range(N-1):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a + b
    heapq.heappush(q, a+b)

print(result)
