# 백준 14425_문자열 집합

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 집합에 포함되는 문자열의 개수, M: 검사해야하는 문자열의 개수
S = [sys.stdin.readline().strip() for _ in range(N)]  # 집합
cnt = 0

for _ in range(M):
    word = sys.stdin.readline().strip()

    if word in S:
        cnt += 1

print(cnt)
