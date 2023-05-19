# 백준 9507_Generations of Tribbles

import sys


t = int(sys.stdin.readline().strip())  # 테스트케이스
koong = [0] * 69
koong[0:4] = [1, 1, 2, 4]
for i in range(4, 69):
    koong[i] = koong[i-1] + koong[i-2] + koong[i-3] + koong[i-4]

for _ in range(t):
    n = int(sys.stdin.readline().strip())  # n 번째
    print(koong[n])
