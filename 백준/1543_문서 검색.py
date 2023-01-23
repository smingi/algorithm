# 백준 1543_문서 검색

import sys


word = sys.stdin.readline().strip()  # 주어진 문자열
find = sys.stdin.readline().strip()  # 찾는 단어
length = len(find)  # 찾는 단어의 길이
result = 0
idx = 0

while idx + length <= len(word):
    if word[idx:idx+length] == find:
        result += 1
        idx += length

    else:
        idx += 1

print(result)
