# 백준 11728_배열 합치기

import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())  # N: 배열 A의 크기, M: 배열 B의 크기
A = deque(map(int, sys.stdin.readline().split()))  # 배열 A
B = deque(map(int, sys.stdin.readline().split()))  # 배열 B
result = deque()

while A and B:
    if A[0] > B[0]:
        result.append(B.popleft())

    else:
        result.append(A.popleft())

if A:
    result += A

if B:
    result += B

print(" ".join(map(str, result)))
