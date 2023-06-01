# 백준 9613_GCD 합

import sys
import math


t = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(t):
    numbers = list(map(int, sys.stdin.readline().split()))  # n, n개의 수
    result = 0

    for i in range(1, len(numbers)):
        for j in range(i+1, len(numbers)):
            result += math.gcd(numbers[i], numbers[j])

    print(result)
