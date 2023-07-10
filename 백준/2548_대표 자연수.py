# 백준 2548_대표 자연수

import sys


N = int(sys.stdin.readline().strip())  # 자연수의 개수
number = sorted(list(map(int, sys.stdin.readline().split())))  # 자연수
left_sum_v, right_sum_v = 0, sum(number) - number[0]*N  # 왼쪽 합, 오른쪽 합
result, min_v = 0, right_sum_v

for i in range(1, N):
    up_height = number[i] - number[i-1]  # 상승한 높이
    left_sum_v += up_height*i  # 올라간 높이만큼 증가
    right_sum_v -= up_height * (N-i)  # 올라간 높이만큼 감소

    # 최소 합이 감소하면 결과 저장
    if left_sum_v + right_sum_v < min_v:
        result = i
        min_v = left_sum_v + right_sum_v

print(number[result])
