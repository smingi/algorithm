# 백준 2581_소수

import sys


def find_prime():  # 에라토스테네스의 체
    prime = []
    sieve = [True] * (N+1)
    sieve[0:2] = [False, False]

    n = int(N**0.5)

    for i in range(2, n+1):
        if sieve[i]:
            for j in range(i+i, N+1, i):
                sieve[j] = False

    for i in range(M, N+1):
        if sieve[i]:
            prime.append(i)

    if prime:
        print(sum(prime))  # 소수의 합
        print(prime[0])  # 소수의 최솟값

    else:
        print(-1)


M = int(sys.stdin.readline().strip())  # M 이상
N = int(sys.stdin.readline().strip())  # N 이하
find_prime()  # M 이상 N 이하 소수찾기
