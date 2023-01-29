# 백준 12850_본대 산책2

import sys


def move(time, start, end):  # 이동
    # 1분이내로 남은 경우
    if time <= 1:
        return connect[1][start][end]

    # 초기값 설정
    connect.setdefault(time, [[0] * 8 for _ in range(8)])

    # 이미 탐색한 경우
    if connect[time][start][end]:
        return connect[time][start][end]

    # 분할 탐색
    left = time // 2
    right = time - left

    # 각각의 경유지 계산
    for i in range(8):
        connect[time][start][end] = (connect[time][start][end] + move(left, start, i) * move(right, i, end)) % mod

    # 탐색이 끝나면 경우의 수 반환
    return connect[time][start][end]


D = int(sys.stdin.readline().strip())  # 주어진 시간(분)
mod = 1000000007  # 나머지를 구할 수

# 연결됨: 1, 연결 안됨: 0
connect = dict()
connect[1] = [
    [0, 1, 1, 0, 0, 0, 0, 0],  # 0: 정보과학관
    [1, 0, 1, 1, 0, 0, 0, 0],  # 1: 전산관
    [1, 1, 0, 1, 1, 0, 0, 0],  # 2: 미래관
    [0, 1, 1, 0, 1, 1, 0, 0],  # 3: 신앙관
    [0, 0, 1, 1, 0, 1, 1, 0],  # 4: 환경직기념관
    [0, 0, 0, 1, 1, 0, 0, 1],  # 5: 진리관
    [0, 0, 0, 0, 1, 0, 0, 1],  # 6: 형남공학관
    [0, 0, 0, 0, 0, 1, 1, 0]   # 7: 학생회관
]

print(move(D, 0, 0))
