# 백준 2776_암기왕

import sys
from collections import defaultdict


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 수첩 1에 적은 개수
    note_one = set(map(int, sys.stdin.readline().split()))  # 수첩 1
    M = int(sys.stdin.readline().strip())  # 수첩 2에 적은 개수
    note_two = list(map(int, sys.stdin.readline().split()))  # 수첩 2
    dic = defaultdict(int)

    for num in note_one:
        dic[num] = 1

    for num in note_two:
        if dic[num]:
            print(1)

        else:
            print(0)
