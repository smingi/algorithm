# 백준 11729_하노이 탑 이동 순서

import sys


def move(n, a, b, c):
    if n == 1:
        print(a, c)

    else:
        move(n-1, a, c, b)
        print(a, c)
        move(n-1, b, a, c)


N = int(sys.stdin.readline().strip())  # 원판의 개수
cnt = 0
for _ in range(N):
    cnt = 2*cnt + 1

print(cnt)
move(N, 1, 2, 3)
