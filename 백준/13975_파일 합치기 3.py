# 백준 13975_파일 합치기 3

import sys
import heapq


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    K = int(sys.stdin.readline().strip())  # 소설의 장수
    size = list(map(int, sys.stdin.readline().split()))  # 파일의 크기
    q = []
    result = 0

    # min heap
    for s in size:
        heapq.heappush(q, s)

    # 파일이 1개로 합쳐질 때까지 작은 파일부터 합치기
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a + b
        heapq.heappush(q, a+b)

    print(result)
