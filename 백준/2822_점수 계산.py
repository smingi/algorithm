# 백준 2822_점수 계산

import sys
import heapq


q = []
for i in range(1, 9):
    score = int(sys.stdin.readline().strip())  # 점수
    heapq.heappush(q, [-score, i])

result = 0
index = []
for _ in range(5):
    score, idx = heapq.heappop(q)
    result += -score
    index.append(idx)

index.sort()

print(result)
print(" ".join(map(str, index)))
