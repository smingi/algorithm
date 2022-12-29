# 백준 1021_회전하는 큐

import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())  # N: 큐의 길이, M: 뽑는 개수
number = list(map(int, sys.stdin.readline().split()))  # 뽑아야하는 위치
q = deque([i for i in range(1, N+1)])
cnt = 0

for num in number:
    while True:
        if q[0] == num:
            q.popleft()
            break

        else:
            # 왼쪽으로 이동
            if q.index(num) <= len(q) // 2:
                q.rotate(-1)
                cnt += 1

            # 오른쪽으로 이동
            else:
                q.rotate(1)
                cnt += 1

print(cnt)
