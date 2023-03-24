# 백준 1431_시리얼 번호

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 기타줄의 개수
q = []
for _ in range(N):
    serial_number = sys.stdin.readline().strip()  # 일련번호
    sumv = 0

    for s in serial_number:
        if s.isdigit():
            sumv += int(s)

    heapq.heappush(q, [len(serial_number), sumv, serial_number])

while q:
    length, sumv, serial_number = heapq.heappop(q)
    print(serial_number)
