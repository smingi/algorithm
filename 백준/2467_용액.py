# 백준 2467_용액

import sys


N = int(sys.stdin.readline().strip())  # 용액의 수
liquid = list(map(int, sys.stdin.readline().split()))  # 용액
left, right = 0, N-1  # 투 포인터
near_nero = abs(liquid[left] + liquid[right])  # 0에 가장 가까운 값
result_l = left  # 왼쪽 부분
result_r = right  # 오른쪽 부분

while left < right:
    now = liquid[left] + liquid[right]  # 현재 값

    if abs(now) < near_nero:  # 0에 더 가까운 값을 찾은 경우
        result_l = left
        result_r = right
        near_nero = abs(now)

        if near_nero == 0:  # 0이 되면 종료
            break

    if now < 0:  # 합이 음수인 경우
        left += 1

    else:  # 합이 양수인 경우
        right -= 1

print(liquid[result_l], liquid[result_r])
