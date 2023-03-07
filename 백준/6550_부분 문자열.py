# 백준 6550_부분 문자열

import sys
from collections import deque


while True:
    word = sys.stdin.readline().strip()

    if not word:
        break

    s, t = word.split()  # 문자열
    q = deque(list(s))

    for word in t:
        if not q:
            break

        if word == q[0]:
            q.popleft()

    if q:
        print("No")

    else:
        print("Yes")
