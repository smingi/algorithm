# 백준 12100_2048 (Easy)

import sys
from copy import deepcopy


def up(now_board):  # 위로 이동
    for c in range(N):  # 열
        pointer = 0

        for r in range(1, N):  # 행
            if now_board[r][c]:  # 움직일 블록이 있는 경우
                tmp = now_board[r][c]
                now_board[r][c] = 0

                if now_board[pointer][c] == 0:  # 비어있는 공간으로 이동하는 경우
                    now_board[pointer][c] = tmp

                elif now_board[pointer][c] == tmp:  # 두 개의 블록이 합쳐지는 경우
                    now_board[pointer][c] *= 2
                    pointer += 1

                else:  # 들어있는 공간으로 이동하는 경우
                    pointer += 1
                    now_board[pointer][c] = tmp

    return now_board


def down(now_board):  # 아래로 이동
    for c in range(N):  # 열
        pointer = N-1

        for r in range(N-2, -1, -1):  # 행
            if now_board[r][c]:  # 움직일 블록이 있는 경우
                tmp = now_board[r][c]
                now_board[r][c] = 0

                if now_board[pointer][c] == 0:  # 비어있는 공간으로 이동하는 경우
                    now_board[pointer][c] = tmp

                elif now_board[pointer][c] == tmp:  # 두 블록이 합쳐지는 경우
                    now_board[pointer][c] *= 2
                    pointer -= 1

                else:  # 들어있는 공간으로 이동하는 경우
                    pointer -= 1
                    now_board[pointer][c] = tmp

    return now_board


def left(now_board):  # 왼쪽으로 이동
    for r in range(N):  # 행
        pointer = 0

        for c in range(1, N):  # 열
            if now_board[r][c]:  # 움직일 블록이 있는 경우
                tmp = now_board[r][c]
                now_board[r][c] = 0

                if now_board[r][pointer] == 0:  # 비어있는 공간으로 이동하는 경우
                    now_board[r][pointer] = tmp

                elif now_board[r][pointer] == tmp:  # 두 블록이 합쳐지는 경우
                    now_board[r][pointer] *= 2
                    pointer += 1

                else:  # 들어있는 공간으로 이동하는 경우
                    pointer += 1
                    now_board[r][pointer] = tmp

    return now_board


def right(now_board):  # 오른쪽으로 이동
    for r in range(N):  # 행
        pointer = N-1

        for c in range(N-2, -1, -1):  # 열
            if now_board[r][c]:
                tmp = now_board[r][c]
                now_board[r][c] = 0

                if now_board[r][pointer] == 0:  # 비어있는 공간으로 이동하는 경우
                    now_board[r][pointer] = tmp

                elif now_board[r][pointer] == tmp:  # 두 블록이 합쳐지는 경우
                    now_board[r][pointer] *= 2
                    pointer -= 1

                else:  # 들어있는 공간으로 이동하는 경우
                    pointer -= 1
                    now_board[r][pointer] = tmp

    return now_board


def move(k, now_board):  # 이동
    global result
    if k == 5:  # 5번 움직인 경우 최댓값 저장하고 종료
        result = max(result, max(map(max, now_board)))
        return

    # 상하좌우 네방향으로 이동
    move(k + 1, up(deepcopy(now_board)))  # 위로 이동
    move(k + 1, down(deepcopy(now_board)))  # 아래로 이동
    move(k + 1, left(deepcopy(now_board)))  # 왼쪽으로 이동
    move(k + 1, right(deepcopy(now_board)))  # 오른쪽으로 이동


N = int(sys.stdin.readline().strip())  # 보드의 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 보드의 상태
result = 0  # 가장 큰 수

move(0, board)  # 이동
print(result)
