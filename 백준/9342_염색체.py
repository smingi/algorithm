# 백준 9342_염색체

import sys
import re


T = int(sys.stdin.readline().strip())  # 테스트케이스
check = re.compile('^[A-F]?A+F+C+[A-F]?$')
# ^: 정규식 시작부분
# [A-F]?: {A, B, C, D, E, F} 중 0개 또는 1개
# A+: A가 하나 또는 그 이상
# F+: F가 하나 또는 그 이상
# C+: C가 하나 또는 그 이상
# [A-F]?: {A, B, C, D, E, F} 중 0개 또는 1개
# $: 정규식 끝부분
for _ in range(T):
    alpha = sys.stdin.readline().strip()

    # 규칙에 맞는 경우
    if check.match(alpha):
        print('Infected!')

    # 규칙에 안 맞는 경우
    else:
        print('Good')
