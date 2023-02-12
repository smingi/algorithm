# 백준 2870_수학숙제

import sys


N = int(sys.stdin.readline().strip())  # 줄의 개수
number_lst = []  # 숫자 리스트
for _ in range(N):
    word = sys.stdin.readline().strip()  # 주어진 단어
    number = ""

    for w in word:
        if w.isalpha():
            if number:
                number_lst.append(int(number))
                number = ""

        else:
            number += w

    if number:
        number_lst.append(int(number))

for num in sorted(number_lst):
    print(num)
