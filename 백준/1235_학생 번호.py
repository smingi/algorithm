# 백준 1235_학생 번호

import sys


def find_cnt():
    for i in range(1, len(number[0]) + 1):
        dic = dict()

        for j in range(N):
            if number[j][-i:] in dic:
                break
            else:
                dic[number[j][-i:]] = 1

        if len(dic) == N:
            return i


N = int(sys.stdin.readline().strip())  # 학생의 수
number = [sys.stdin.readline().strip() for _ in range(N)]
print(find_cnt())
