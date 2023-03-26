# 백준 11004_K번째 수

import sys


N, K = map(int, sys.stdin.readline().split())  # 숫자의 개수, K번째 수
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
print(numbers[K-1])
