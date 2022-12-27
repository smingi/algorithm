# 백준 1011_Fly me to the Alpha Centauri

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())  # 시작위치, 도착위치
    distance = y - x  # 두 지점 사이의 거리
    n = 0

    while True:
        if distance <= n * (n+1):
            break

        n += 1

    if distance <= n**2:
        print(n*2-1)

    else:
        print(n*2)
