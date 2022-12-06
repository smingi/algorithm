# 백준 1759_암호 만들기

import sys
from itertools import combinations


L, C = map(int, sys.stdin.readline().split())  # L: 암호의 길이, C: 문자의 개수
words = list(sys.stdin.readline().split())  # 주어진 문자열
words.sort()  # 알파벳을 순서대로 정렬
vowel = ["a", "e", "i", "o", "u"]  # 알파벳 모음

for combination in combinations(words, L):
    vowel_cnt = 0  # 모음 개수
    consonant_cnt = 0  # 자음 개수

    for word in combination:
        if word in vowel:
            vowel_cnt += 1

        else:
            consonant_cnt += 1

    # 한 개 이상의 모음과 두 개 이상의 자음으로 이루어지면 출력
    if vowel_cnt > 0 and consonant_cnt > 1:
        print("".join(combination))
