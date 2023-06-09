# 백준 1449_수리공 항승

import sys


N, L = map(int, sys.stdin.readline().split())  # N: 물이 새는 곳의 개수, L: 테이프의 길이
location = sorted(list(map(int, sys.stdin.readline().split())))  # 물이 새는 곳의 위치
tape = 0  # 테이프의 위치
result = 0  # 테이프의 개수

for i in range(N):
    if location[i] > tape:
        result += 1
        tape = location[i] + L - 0.5

print(result)
