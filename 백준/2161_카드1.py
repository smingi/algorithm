# 백준 2161_카드1

import sys
from collections import deque


n = int(sys.stdin.readline().strip())  # 정수
q = deque([i for i in range(1, n+1)])
result = []

while len(q) > 1:
    result.append(q.popleft())
    q.append(q.popleft())

result.append(q.popleft())
print(" ".join(map(str, result)))
