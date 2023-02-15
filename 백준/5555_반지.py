# 백준 5555_반지

import sys


find_word = sys.stdin.readline().strip()  # 찾아야 하는 문자열
N = int(sys.stdin.readline().strip())  # 반지의 개수
result = 0

for _ in range(N):
    ring = sys.stdin.readline().strip()  # 반지

    if find_word in ring+ring:
        result += 1

print(result)
