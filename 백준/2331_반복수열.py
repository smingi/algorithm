# 백준 2331_반복수열

import sys


# 다음 숫자 계산
def find_number(number):
    sum_v = 0

    for num in str(number):
        sum_v += int(num) ** P

    return sum_v


A, P = map(int, sys.stdin.readline().split())  # A: 수, P: 제곱수
result = [A]

while True:
    new = find_number(result[-1])

    if new in result:
        print(result.index(new))
        break

    else:
        result.append(new)
