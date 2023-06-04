# 백준 1049_기타줄

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 끊어진 기타줄의 개수 , M: 기타줄 브랜드의 개수
set_cost = 1001
one_cost = 1001

for _ in range(M):
    s, o = map(int, sys.stdin.readline().split())  # 기타줄의 가격(s: 6개, o: 1개)
    set_cost = min(set_cost, s)
    one_cost = min(one_cost, o)

if set_cost < 6 * one_cost:
    if set_cost < (N % 6 * one_cost):
        print((N // 6 + 1) * set_cost)

    else:
        print((N // 6 * set_cost) + (N % 6 * one_cost))

else:
    print(N * one_cost)
