# 백준 2346_풍선 터뜨리기

import sys
from collections import deque


N = int(sys.stdin.readline().strip())  # 풍선의 개수
paper = list(map(int, sys.stdin.readline().split()))  # 풍선에 적힌 종이
q = deque([i+1, val] for i, val in enumerate(paper))

while q:
    idx, num = q.popleft()
    print(idx, end=" ")

    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)

print()
