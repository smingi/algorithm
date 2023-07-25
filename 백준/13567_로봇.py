# 백준 13567_로봇

import sys


def move():
    r, c = 0, 0
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    idx = 0

    for _ in range(n):
        command, code = sys.stdin.readline().split()  # 명령어

        # 이동
        if command == 'MOVE':
            new_r = r + dr[idx] * int(code)
            new_c = c + dc[idx] * int(code)

            # 이동 가능한 경우
            if 0 <= new_r <= M and 0 <= new_c <= M:
                r = new_r
                c = new_c

            else:
                print(-1)
                return

        # 방향전환
        elif command == 'TURN':
            # 왼쪽
            if code == '0':
                idx = (4 + idx - 1) % 4

            # 오른쪽
            elif code == '1':
                idx = (idx + 1) % 4

    print(c, r)
    return


M, n = map(int, sys.stdin.readline().split())  # M: 정사각형의 크기, n: 명령어 수
move()
