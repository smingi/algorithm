# 백준 11000_강의실 배정

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 강의 개수
lecture = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 강의(시작, 종료)
lecture.sort()
q = []
heapq.heappush(q, lecture[0][1])  # 첫 강의

for i in range(1, N):

    # 이어서 강의를 할 수 있는 경우 이전 강의 빼기
    if q[0] <= lecture[i][0]:
        heapq.heappop(q)

    heapq.heappush(q, lecture[i][1])

print(len(q))
