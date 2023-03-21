# 백준 2217_로프

import sys


N = int(sys.stdin.readline().strip())  # 로프의 개수
rope = [int(sys.stdin.readline().strip()) for _ in range(N)]  # 로프
rope.sort()

result = 0
for i in range(N):
    result = max(result, rope[i] * (N-i))

print(result)
