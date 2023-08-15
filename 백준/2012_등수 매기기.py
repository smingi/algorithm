# 백준 2012_등수 매기기

import sys


N = int(sys.stdin.readline().strip())  # 학생의 수
rank = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])  # 등수
result = 0

for i in range(N):
    result += abs(i+1-rank[i])

print(result)
