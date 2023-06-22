# 백준 2503_숫자 야구

import sys
from itertools import permutations


N = int(sys.stdin.readline().strip())  # 질문 횟수
permutation = list(permutations([str(i) for i in range(1, 10)], 3))

for _ in range(N):
    number, strike, ball = sys.stdin.readline().split()  # 질문 숫자, 스트라이크, 볼
    remove_cnt = 0  # 제거한 개수

    for i in range(len(permutation)):
        now_strike, now_ball = 0, 0  # 현재 스트라이크, 볼
        idx = i - remove_cnt  # 현재 인덱스

        for j in range(3):
            # 스트라이크인 경우
            if permutation[idx][j] == number[j]:
                now_strike += 1

            # 볼인 경우
            elif number[j] in permutation[idx]:
                now_ball += 1

        # 조건에 맞지 않는 경우 제거
        if now_strike != int(strike) or now_ball != int(ball):
            permutation.remove(permutation[idx])
            remove_cnt += 1

print(len(permutation))
