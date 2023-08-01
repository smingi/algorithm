# 백준 11501_주식

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 날의 수
    stock = list(map(int, sys.stdin.readline().split()))  # 주가
    result = 0
    max_v = stock[-1]

    for i in range(N-2, -1, -1):
        if stock[i] > max_v:
            max_v = stock[i]

        else:
            result += max_v - stock[i]

    print(result)
