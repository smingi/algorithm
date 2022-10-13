# 백준 2239_스도쿠 (pypy3 사용)

import sys


def valid_check(check_r, check_c, check_number):  # 조건 만족 여부
    # 가로, 새로
    for i in range(9):
        if sudoku[check_r][i] == check_number:
            return False

        if sudoku[i][check_c] == check_number:
            return False

    # 3*3 내부
    r = check_r // 3 * 3
    c = check_c // 3 * 3

    for i in range(r, r+3):
        for j in range(c, c+3):
            if sudoku[i][j] == check_number:
                return False

    return True


def find_available_number(now_r, now_c):  # 사용가능한 숫자 찾기 및 반환
    available_number = []  # 사용가능한 숫자 목록

    for number in range(1, 10):
        if valid_check(now_r, now_c, number):  # 타당성 체크
            available_number.append(number)

    return available_number  # 사용가능한 숫자 목록 반환


def dfs(k):  # 깊이 우선 탐색, k: 스도쿠에 넣은 숫자 개수
    global is_completed

    if k == len(empty):  # 스도쿠가 다 채워지면
        is_completed = True  # 완료체크
        return

    now_r, now_c = empty[k][0], empty[k][1]  # 현재 행과 열위치
    now_available_number = find_available_number(now_r, now_c)  # 현 위치에서 사용가능한 숫자 찾기

    for number in now_available_number:  # 사용가능한 숫자를 모두 대입
        sudoku[now_r][now_c] = number
        dfs(k+1)

        if is_completed:  # 숫자를 다 채우면 종료
            return

        sudoku[now_r][now_c] = 0


sudoku = []  # 스도쿠 상태
empty = []  # 스도쿠에 비어있는 위치

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().strip())))  # 입력받은 스도쿠 상태

    for j in range(9):  # 스도쿠에 비어있는 위치 찾기
        if sudoku[i][j] == 0:
            empty.append([i, j])


is_completed = False  # 스도쿠가 완성됐는지 여부
dfs(0)

for i in range(9):
    print("".join(map(str, sudoku[i])))
