# 백준 8911_거북이

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
# 방향
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for _ in range(T):
    command = sys.stdin.readline().strip()  # 명령어
    direction = 0  # 방향 인덱스
    min_r, max_r, min_c, max_c = 0, 0, 0, 0  # 행, 열(최대/최소)
    now_r, now_c = 0, 0  # 행, 열(현재)

    for c in command:
        # F: 한 눈금 앞으로
        if c == 'F':
            now_r += dr[direction]
            now_c += dc[direction]

        # B: 한 눈금 뒤로
        elif c == 'B':
            now_r -= dr[direction]
            now_c -= dc[direction]

        # L: 왼쪽으로 90도 회전
        elif c == 'L':
            direction = (4 + direction - 1) % 4

        # R: 오른쪽으로 90도 회전
        elif c == 'R':
            direction = (direction + 1) % 4

        # 행, 열(최대/최소)
        min_r, max_r, min_c, max_c = min(min_r, now_r), max(max_r, now_r), min(min_c, now_c), max(max_c, now_c)

    print(abs(max_r - min_r) * abs(max_c - min_c))
