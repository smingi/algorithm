# 백준 10867_중복 빼고 정렬하기

import sys


N = int(sys.stdin.readline().strip())  # 수의 개수
numbers = list(set(map(int, sys.stdin.readline().split())))  # 숫자
numbers.sort()
print(" ".join(map(str, numbers)))
