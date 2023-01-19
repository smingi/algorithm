# 백준 10815_숫자 카드

import sys


N = int(sys.stdin.readline().strip())  # 상근이가 가지고 있는 숫자 카드의 개수
card = list(map(int, sys.stdin.readline().split()))  # 상근이가 가지고 있는 숫자 카드
M = int(sys.stdin.readline().strip())  # 상근이가 가지고 있는지 확인할 숫자 카드의 개수
find = list(map(int, sys.stdin.readline().split()))  # 상근이가 가지고 있는지 확인할 숫자 카드

dic = dict()
for c in card:
    dic[c] = 1

for f in find:
    if f not in dic:
        print(0, end=" ")

    else:
        print(1, end=" ")
