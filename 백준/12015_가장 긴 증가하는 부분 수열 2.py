# 백준 120115_가장 긴 증가하는 부분 수열 2

import sys


A = int(sys.stdin.readline().strip())  # 수열의 크기
sequence = [0] + list(map(int, sys.stdin.readline().split()))  # 수열
memoization = [0]

for num in sequence:
    if memoization[-1] < num:
        memoization.append(num)

    else:
        left = 0
        right = len(memoization)

        while left < right:
            mid = (left + right) // 2

            if memoization[mid] < num:
                left = mid + 1
            else:
                right = mid

        memoization[right] = num

print(len(memoization) - 1)
