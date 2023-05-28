# 백준 2018_수들의 합 5

import sys


N = int(sys.stdin.readline().strip())  # 자연수
s, e = 0, 0
cnt, sum_v = 0, 0

while e <= N:
    if sum_v < N:
        e += 1
        sum_v += e

    elif sum_v > N:
        sum_v -= s
        s += 1

    else:
        cnt += 1
        e += 1
        sum_v += e

print(cnt)
