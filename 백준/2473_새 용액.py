# 백준 2437_새 용액

import sys


N = int(sys.stdin.readline().strip())  # 용액의 수
liquid = list(map(int, sys.stdin.readline().split()))  # 용액
liquid.sort()  # 정렬
near_zero = sys.maxsize  # 0에 가장 가까운 수
result = []  # 결과

for i in range(N-2):
    mid = i + 1  # 중간지점
    right = N - 1  # 오른쪽 지점

    while mid < right:
        now = liquid[i] + liquid[mid] + liquid[right]  # 현재 값

        if abs(now) < near_zero:  # 0에 더 가까워진 경우
            near_zero = abs(now)
            result = [liquid[i], liquid[mid], liquid[right]]

        if now < 0:  # 음수인 경우
            mid += 1

        elif now > 0:  # 양수인 경우
            right -= 1

        else:  # 0이 되는 경우
            break

print(" ".join(map(str, result)))
