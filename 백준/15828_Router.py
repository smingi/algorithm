# 백준 15828_Router

import sys
from collections import deque


N = int(sys.stdin.readline().strip())  # 버퍼의 크기
q = deque()

while True:
    info = int(sys.stdin.readline().strip())  # 처리해야할 정보

    # 종료
    if info == -1:
        break

    # 처리
    elif info == 0 and q:
        q.popleft()

    # 입력
    elif info and len(q) < N:
        q.append(info)

if q:
    print(" ".join(map(str, q)))

else:
    print("empty")
