# 백준 2089_-2진수

import sys


def to_binary(number):
    if number == 0:
        return 0

    result = ''
    while number:
        result += str(number % 2)
        number //= 2
        number *= -1

    return result[::-1]


N = int(sys.stdin.readline().strip())  # 십진수
print(to_binary(N))
