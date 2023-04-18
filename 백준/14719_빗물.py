# 백준 14719_빗물

import sys


H, W = map(int, sys.stdin.readline().split())  # H: 세로, W: 가로
height = list(map(int, sys.stdin.readline().split()))  # 높이
result = 0

for i in range(1, W-1):
    # 왼쪽 벽
    left = max(height[:i])

    # 오른쪽 벽
    right = max(height[i+1:])

    # 둘 중 낮은 높이
    min_height = min(left, right)

    # 현재 높이가 낮은 높이보다 낮은 경우
    if min_height > height[i]:
        result += min_height - height[i]

print(result)
