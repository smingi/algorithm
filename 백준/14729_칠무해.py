# 백준 14729_칠무해

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 학생의 수
q = []
for _ in range(N):
    heapq.heappush(q, float(sys.stdin.readline().strip()))  # 점수

for _ in range(7):
    print("{0:.3f}".format(heapq.heappop(q)))
