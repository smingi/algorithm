# 백준 1476_날짜 계산

import sys


E, S, M = map(int, sys.stdin.readline().split())  # E: 지구, S: 태양, M: 달
year = 1

while True:
    if ((year-E) % 15 == 0) and ((year-S) % 28 == 0) and ((year-M) % 19 == 0):
        break

    year += 1

print(year)
