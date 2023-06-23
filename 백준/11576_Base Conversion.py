# 백준 11576_Base Conversion

import sys


A, B = map(int, sys.stdin.readline().split())  # 진법
m = int(sys.stdin.readline().strip())  # 자릿수
number = list(map(int, sys.stdin.readline().split()))  # 숫자
sum_v = 0
number.reverse()

for i in range(m):
    sum_v += number[i] * (A**i)

result = []
while sum_v // B:
    result.append(sum_v % B)
    sum_v //= B

result.append(sum_v)
result.reverse()

print(" ".join(map(str, result)))
