# 백준 1913_달팽이

import sys


N = int(sys.stdin.readline().strip())  # N * N
num = int(sys.stdin.readline().strip())  # 찾아야하는 수
board = [[0] * N for _ in range(N)]
r, c = N//2, N//2
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
idx = 3
result = [0, 0]

# 기준점(이동한 거리), 다음목표(이동할 거리), 횟수(0, 1)
now, target, cnt = 0, 0, -1
for i in range(1, (N*N)+1):
    # 숫자 체크
    board[r][c] = i

    # 찾는 숫자인 경우
    if i == num:
        result[0], result[1] = r+1, c+1

    # 2번 방향을 바꿀 때마다 이동거리 1씩 증가
    if now == target:
        # 방향전환
        idx = (idx+1) % 4

        # 방향을 2번 바꾸면 다음목표 +1
        if cnt == 1:
            now = 0
            target += 1
            cnt = 0
        else:
            now = 0
            cnt += 1
    else:
        # 이동거리 +1
        now += 1

    # 다음 방향으로 이동
    r += dr[idx]
    c += dc[idx]

# 결과 출력
for i in range(N):
    print(*board[i])
print(result[0], result[1])
