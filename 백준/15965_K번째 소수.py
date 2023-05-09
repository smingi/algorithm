# 백준 15965_K번째 소수

import sys


K = int(sys.stdin.readline().strip())  # K 번째 소수
cnt = 0
INF = int(1e7)
sieve = [True] * INF

for i in range(2, INF):
    if sieve[i]:
        cnt += 1

        if cnt == K:
            print(i)
            break

        for j in range(i+i, INF, i):
            sieve[j] = False
