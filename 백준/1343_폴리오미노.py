# 백준 1343_폴리오미노

import sys


word = sys.stdin.readline().strip()  # 입력받은 문자열
word = word.replace('XXXX', 'AAAA')
word = word.replace('XX', 'BB')

if 'X' in word:
    print(-1)

else:
    print(word)
