# 백준 2670_연속부분최대곱

import sys


N = int(sys.stdin.readline().strip())  # 실수의 개수
number = [float(sys.stdin.readline().strip()) for _ in range(N)]

for i in range(1, N):
    number[i] = max(number[i], number[i] * number[i-1])

print('{0:.3f}'.format(max(number)))
