# 백준 16435_스네이크버드

import sys


N, L = map(int, sys.stdin.readline().split())  # N: 과일의 개수, L: 초기 길이
fruit = sorted(list(map(int, sys.stdin.readline().split())))  # 과일

for i in range(N):
    if L >= fruit[i]:
        L += 1

    else:
        break

print(L)
