# 백준 1010_다리 놓기

import sys


T = int(sys.stdin.readline().strip())  # 테스트 케이스
for _ in range(T):
    w, e = map(int, sys.stdin.readline().split())  # w: 서쪽, e: 동쪽

    result = 1  # 결과
    for i in range(e, w, -1):  # 분자
        result *= i
    for j in range(e - w, 1, -1):  # 분모
        result //= j

    print(result)
