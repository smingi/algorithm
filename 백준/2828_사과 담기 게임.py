# 백준 2828_사과 담기 게임

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 스크린 넓이, M: 바구니 크기
J = int(sys.stdin.readline().strip())  # 사과의 개수
s, e = 1, M  # 바구니의 위치
result = 0

for _ in range(J):
    apple = int(sys.stdin.readline().strip())  # 사과 위치

    # 사과가 바구니 왼쪽에 있는 경우
    if apple < s:
        result += (s - apple)
        s = apple
        e = apple + M - 1

    # 사과가 바구니 오른쪽에 있는 경우
    elif e < apple:
        result += (apple - e)
        e = apple
        s = e - M + 1

print(result)
