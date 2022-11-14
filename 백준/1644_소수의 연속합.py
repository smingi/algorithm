# 백준 1644_소수의 연속합

import sys


def get_prime():  # 에라토스테네스의 체
    primes = []
    sieve = [True] * (N+1)

    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, N+1, i):
                sieve[j] = False

    for i in range(2, N+1):
        if sieve[i]:
            primes.append(i)

    return primes


N = int(sys.stdin.readline().strip())  # 자연수
prime = get_prime()  # 소수 찾기

result = 0
s, e = 0, 1  # 시작지점, 끝지점
while e <= len(prime):
    tmp = sum(prime[s:e])  # 현재합

    if tmp == N:  # 자연수 N을 만든경우
        result += 1
        e += 1

    elif tmp < N:  # 자연수 N보다 작은 경우
        e += 1

    else:  # 자연수 N보다 큰 경우
        s += 1

print(result)
