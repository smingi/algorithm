# 백준 11656_접미사 배열

import sys


word = sys.stdin.readline().strip()  # 입력받은 문자열
result = []

for i in range(len(word)):
    result.append(word[i:len(word)])

result.sort()

for r in result:
    print(r)
