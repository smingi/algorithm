# 백준 4948_베르트랑 공준

import sys


# 소수 찾기
def find_prime():
    for i in range(2, max_v):
        if sieve[i]:
            for j in range(i+i, max_v, i):
                sieve[j] = 0


max_v = 246913
sieve = [1] * max_v
sieve[0:2] = [0, 0]
find_prime()


while True:
    n = int(sys.stdin.readline().strip())  # n+1 ~ 2n

    # 종료조건
    if n == 0:
        break

    print(sum(sieve[n+1:2*n+1]))
