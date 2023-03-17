# 백준 1963_소수 경로

import sys
from collections import deque


def find_target():  # 목표 소수 찾기
    visited = [0] * 10000
    q = deque()
    q.append([start, 0])
    visited[start] = 1

    while q:
        now, cnt = q.popleft()

        if now == target:
            return cnt

        tmp = str(now)
        for i in range(4):
            for j in range(10):
                new = int(tmp[:i] + str(j) + tmp[i+1:])

                if new >= 1000 and sieve[new] and not visited[new]:
                    q.append([new, cnt+1])
                    visited[new] = 1

    return "Impossible"


def find_prime():  # 에라토스테네스의 체
    sieve[0:2] = [0, 0]
    for i in range(2, 10000):
        if sieve[i]:
            for j in range(i+i, 10000, i):
                sieve[j] = 0


T = int(sys.stdin.readline().strip())  # 테스트케이스
sieve = [1] * 10000  # 소수는 1
find_prime()  # 소수찾기
for _ in range(T):
    start, target = map(int, sys.stdin.readline().split())  # 시작소수, 목표소수
    print(find_target())
