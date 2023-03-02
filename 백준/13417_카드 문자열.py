# 백준 13417_카드 문자열

import sys
from collections import deque


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 카드의 개수
    card = list(sys.stdin.readline().split())  # 카드
    q = deque()
    q.append(card[0])

    for i in range(1, N):
        if card[i] <= q[0]:
            q.appendleft(card[i])

        else:
            q.append(card[i])

    print("".join(q))
