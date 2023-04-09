# 백준 15688_수 정렬하기 5

import sys


N = int(sys.stdin.readline().strip())  # 숫자의 개수
number = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

for num in number:
    print(num)
