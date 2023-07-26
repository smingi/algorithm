# 백준 17143_낚시왕

import sys


def find_new_location(now_r, now_c, now_s, now_d):  # 이동한 상어 위치 찾기
    # 1: 위, 2: 아래
    if now_d == 1 or now_d == 2:

        # 반복 구간
        cycle = R * 2 - 2

        if now_d == 1:
            now_s += cycle - now_r

        else:
            now_s += now_r

        now_s %= cycle
        if now_s >= R:
            now_r = cycle - now_s
            now_d = 1

        else:
            now_r = now_s
            now_d = 2

    # 3: 오른쪽, 4: 왼쪽
    else:

        # 반복 구간
        cycle = C * 2 - 2

        if now_d == 4:
            now_s += cycle - now_c

        else:
            now_s += now_c

        now_s %= cycle
        if now_s >= C:
            now_c = cycle - now_s
            now_d = 4

        else:
            now_c = now_s
            now_d = 3

    return now_r, now_c, now_d


def move_shark():  # 상어 이동하기
    global board

    # 상어가 새로 이동한 위치
    new_board = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]

    # 상어 위치 찾기 + 새로운 위치로 이동
    for i in range(R):
        for j in range(C):
            if board[i][j][2]:
                new_r, new_c, new_d = find_new_location(i, j, board[i][j][0], board[i][j][1])

                # 한 자리에 제일 큰 상어만 있도록 저장
                if new_board[new_r][new_c][2] < board[i][j][2]:
                    new_board[new_r][new_c] = [board[i][j][0], new_d, board[i][j][2]]

    # 상어 위치 갱신
    board = new_board


def catch_shark(col):  # 상어 잡기
    global result

    # 가장 땅에 가까운 상어 잡기
    for row in range(R):
        if board[row][col][2]:
            result += board[row][col][2]
            board[row][col] = [0, 0, 0]
            break


R, C, M = map(int, sys.stdin.readline().split())  # R: 행, C: 열, M: 상어의 수
board = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]  # 보드판
for _ in range(M):
    # r: 행, c: 열, s: 속력, d: 이동방향(1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽), z: 크기
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = [s, d, z]  # 속력, 이동방향, 크기

result = 0

# 시뮬레이션
for angler in range(C):  # 1. 낚시꾼 이동
    catch_shark(angler)  # 2. 상어 잡기
    move_shark()  # 3. 상어 이동

print(result)
