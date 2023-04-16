# 백준 15904_UCPC는 무엇의 약자일까?

import sys


word = sys.stdin.readline().strip()
target = ['U', 'C', 'P', 'C']
index = 0

for w in word:
    if index == 4:
        break

    if w == target[index]:
        index += 1

if index == 4:
    print("I love UCPC")

else:
    print("I hate UCPC")
