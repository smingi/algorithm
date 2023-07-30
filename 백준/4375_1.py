# 백준 4375_1

import sys


def find_length(num):
    if num == 1:
        return 1

    length = 1
    tmp = 1
    while True:
        tmp += pow(10, length)
        length += 1

        if int(tmp % num) == 0:
            return length


while True:
    number = sys.stdin.readline().strip()

    if not number:
        break

    print(find_length(int(number)))
