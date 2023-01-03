# 백준 1799_비숍

import sys


def dfs(r, c, cnt):
    global max_cnt

    # 다음 칸이 다른 행으로 넘어가는 경우
    if n % 2:  # n이 홀수인 경우
        if c == n:  # 열의 크기보다 1칸 많은 경우
            r += 1
            c = 0

        elif c == n+1:  # 열의 크기보다 2칸 많은 경우
            r += 1
            c = 1

    else:  # n이 짝수인 경우
        if c == n:  # 열의 크기보다 1칸 많은 경우
            r += 1
            c = 1

        elif c == n+1:  # 열의 크기보다 2칸 많은 경우
            r += 1
            c = 0

    if r == n:  # 탐색이 끝난 경우
        max_cnt = max(max_cnt, cnt)  # 최대 개수 저장 및 종료
        return

    # 놓을 수 있는 경우
    if board[r][c] == 1 and not visited[0][r + c] and not visited[1][r - c]:
        visited[0][r + c] = 1
        visited[1][r - c] = 1
        dfs(r, c + 2, cnt + 1)
        visited[0][r + c] = 0
        visited[1][r - c] = 0

    # 놓을 수 없는 경우
    dfs(r, c + 2, cnt)


n = int(sys.stdin.readline().strip())  # 체스판의 크기 (n*n)
# 체스판 (1: 놓을 수 있음, 0: 놓을 수 없음)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * (n*2) for _ in range(2)]

# 첫번째 칸 색(흰색)만 탐색
max_cnt = 0  # 최대 놓을 수 있는 개수
dfs(0, 0, 0)
white_cnt = max_cnt  # 흰색 칸에 놓을 수 있는 최대 개수

# 두번째 칸 색(검은색)만 탐색
max_cnt = 0  # 최대 놓을 수 있는 개수
dfs(0, 1, 0)
black_cnt = max_cnt  # 검은색 칸에 놓을 수 있는 최대 개수

print(white_cnt + black_cnt)
