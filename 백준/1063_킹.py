# 백준 1063_킹

import sys


king, rock, N = sys.stdin.readline().split()  # 킹의 위치, 돌의 위치, 이동 횟수

# 숫자 위치로 변경
k = [int(king[1])-1, ord(king[0]) - ord('A')]  # 킹의 위치
r = [int(rock[1])-1, ord(rock[0]) - ord('A')]  # 돌의 위치

# 이동 방향
dic = {
    'R': [0, 1],     # 한 칸 오른쪽으로
    'L': [0, -1],    # 한 칸 왼쪽으로
    'B': [-1, 0],    # 한 칸 아래로
    'T': [1, 0],     # 한 칸 위로
    'RT': [1, 1],    # 오른쪽 위 대각선으로
    'LT': [1, -1],   # 왼쪽 위 대각선으로
    'RB': [-1, 1],   # 오른쪽 아래 대각선으로
    'LB': [-1, -1],  # 왼쪽 아래 대각선으로
}

for _ in range(int(N)):
    command = sys.stdin.readline().strip()  # 이동 위치

    dr, dc = dic[command]  # 이동위치
    new_kr, new_kc = k[0] + dr, k[1] + dc  # 새로운 킹의 위치

    # 새로운 킹의 위치가 범위 안인 경우
    if 0 <= new_kr < 8 and 0 <= new_kc < 8:

        # 돌이 있는 경우
        if r[0] == new_kr and r[1] == new_kc:
            new_rr, new_rc = r[0] + dr, r[1] + dc  # 새로운 돌의 위치

            # 새로운 돌의 위치가 범위 안인 경우
            if 0 <= new_rr < 8 and 0 <= new_rc < 8:
                r = [new_rr, new_rc]
                k = [new_kr, new_kc]

        # 돌이 없는 경우
        else:
            k = [new_kr, new_kc]

print(chr(k[1] + ord('A')) + str(k[0] + 1))
print(chr(r[1] + ord('A')) + str(r[0] + 1))
