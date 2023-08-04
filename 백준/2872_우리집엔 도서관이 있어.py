# 백준 2872_우리집엔 도서관이 있어

import sys


N = int(sys.stdin.readline().strip())  # 책의 수
book = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = N
result = 0

for i in range(N-1, -1, -1):
    if book[i] != res:
        result += 1
    else:
        res -= 1

print(result)
