# 백준 2096_내려가기

import sys


N = int(sys.stdin.readline().strip())  # N: 줄수
max_score = [0] * 3  # 최대 점수
min_score = [0] * 3  # 최소 점수
temp_max_score = [0] * 3  # 임시 최대 점수
temp_min_score = [0] * 3  # 임시 최소 점수

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())  # 칸 별 점수

    # 최대 점수 구하기
    temp_max_score[0] = a + max(max_score[0], max_score[1])
    temp_max_score[1] = b + max(max_score[0], max_score[1], max_score[2])
    temp_max_score[2] = c + max(max_score[1], max_score[2])

    # 최소 점수 구하기
    temp_min_score[0] = a + min(min_score[0], min_score[1])
    temp_min_score[1] = b + min(min_score[0], min_score[1], min_score[2])
    temp_min_score[2] = c + min(min_score[1], min_score[2])

    for i in range(3):  # 구한 점수 저장
        max_score[i] = temp_max_score[i]
        min_score[i] = temp_min_score[i]

print(max(max_score), min(min_score))  # 최대, 최소 점수 출력
