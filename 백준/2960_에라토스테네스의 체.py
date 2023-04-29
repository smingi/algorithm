# 백준 2960_에라토스테네스의 체

import sys


def find():
    cnt = 0
    sieve = [True] * (N + 1)

    for i in range(2, N+1):
        for j in range(i, N+1, i):
            if sieve[j]:
                sieve[j] = False
                cnt += 1

                if cnt == K:
                    return j


N, K = map(int, sys.stdin.readline().split())  # N: 2부터 N 까지의 정수, K: 번쨰
print(find())
