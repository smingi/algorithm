# 백준 1544_사이클 단어

import sys
from collections import deque


N = int(sys.stdin.readline().strip())  # 단어의 수
words = set()  # 단어목록
words.add(sys.stdin.readline().strip())  # 첫 단어

for _ in range(N-1):
    word = deque(sys.stdin.readline().strip())  # 단어
    is_new = True

    for _ in range(len(word)):
        rotation = ''.join(word)

        if rotation in words:
            is_new = False
            break

        else:
            word.rotate()

    if is_new:
        words.add(''.join(word))

print(len(words))
