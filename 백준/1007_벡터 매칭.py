# 백준 1007_벡터 매칭

import sys
from itertools import combinations


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 점의 개수(짝수)
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 점의 좌표
    total_sum_x = 0  # x값의 총합
    total_sum_y = 0  # y값의 총합

    # x, y의 총합 구하기
    for x, y in points:
        total_sum_x += x
        total_sum_y += y

    min_v = int(1e9)  # 백터의 합의 길이의 최솟값
    combination = list(combinations(points, N//2))  # 조합

    for comb in combination[:len(combination)//2]:
        now_sum_x = 0  # 현재 x값의 합
        now_sum_y = 0  # 현재 y값의 합

        # 현재 x, y값의 합 구하기
        for x, y in comb:
            now_sum_x += x
            now_sum_y += y

        dif_sum_x = total_sum_x - now_sum_x  # 총 x값의 합과 현재 x값의 합의 차 구하기
        dif_sum_y = total_sum_y - now_sum_y  # 총 y값의 합과 현재 y값의 합의 차 구하기

        # 백터의 합의 길이의 최솟값 저장
        min_v = min(min_v, (((now_sum_x - dif_sum_x) ** 2 + (now_sum_y - dif_sum_y) ** 2) ** 0.5))

    print(min_v)
