# 백준 1500_최대 곱

import sys


S, K = map(int, sys.stdin.readline().split())  # S: 합, K: 개수
quotient = S // K  # 몫
remainder = S % K  # 나머지
result = 1

for _ in range(K):
    if remainder:
        result *= quotient + 1
        remainder -= 1

    else:
        result *= quotient

print(result)
