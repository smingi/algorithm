# 백준 11256_사탕

import sys
import heapq


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    J, N = map(int, sys.stdin.readline().split())  # J: 사탕의 개수, N: 상자의 개수
    q = []

    for _ in range(N):
        r, c = map(int, sys.stdin.readline().split())  # r: 세로, c: 가로
        heapq.heappush(q, -r*c)

    result = 0
    while J > 0:
        result += 1
        box = -heapq.heappop(q)
        J -= box

    print(result)
