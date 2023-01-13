# 백준 9527_1의 개수 세기

import sys


def count_one(num):  # 1의 개수 세기
    cnt = 0  # 1의 개수
    power = 0  # 분석할 자릿수
    # ex) power = 0: 1의 자릿수, power = 1: 10의 자릿수

    while 2**power <= (num+1):
        pattern_length = 2**(power+1)  # 패턴의 길이

        # 완성 패턴의 1의 개수
        # ex) 패턴이 0011이면 0011인 부분
        complete_pattern_cnt = (num+1) // pattern_length  # 완성된 패턴의 개수
        cnt += complete_pattern_cnt * (pattern_length//2)  # (완성된 패턴의 개수 * 완성된 패턴의 1의 개수)

        # 미완성 패턴의 1의 개수
        # ex) 패턴이 0011이면 0, 00, 001인 부분
        incomplete_pattern_length = (num+1) % pattern_length  # 미완성 패턴의 길이
        cnt += max(0, incomplete_pattern_length - pattern_length//2)  # (미완성 패턴의 길이 - 완성된 패턴의 절반 길이)

        # 다음 자릿수
        power += 1

    return cnt


A, B = map(int, sys.stdin.readline().split())  # 두 자연수 (1 ≤ A ≤ B ≤ 10**16)
# A이상 B 이하의 수의 1의 개수(0부터 B 까지의 1의 개수 - 0부터 A-1까지의 1의 개수)
print(count_one(B) - count_one(A-1))
