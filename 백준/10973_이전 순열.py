# 백준 10973_이전 순열

import sys


def solve():
    number = list(map(int, sys.stdin.readline().split()))

    for i in range(N - 1, 0, -1):
        if number[i] < number[i - 1]:
            for j in range(N - 1, 0, -1):
                if number[j] < number[i-1]:
                    number[j], number[i-1] = number[i-1], number[j]
                    number = number[:i] + sorted(number[i:], reverse=True)
                    return ' '.join(map(str, number))

    return -1


N = int(sys.stdin.readline().strip())  # 1 ~ N
print(solve())
