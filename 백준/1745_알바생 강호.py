# 백준 1745_알바생 강호

import sys


N = int(sys.stdin.readline().strip())  # 사람수
tip = sorted([int(sys.stdin.readline().strip()) for _ in range(N)], reverse=True)  # 팁
result = 0

for i in range(N):
    if tip[i] - i > 0:
        result += (tip[i] - i)

print(result)
