# 백준 2805_나무 자르기

import sys


N, M = map(int, sys.stdin.readline().split())  # N: 나무 개수, M: 필요한 길이
tree = list(map(int, sys.stdin.readline().split()))  # 나무 높이 리스트

st = 1
ed = max(tree)

while st <= ed:  # 이분 탐색
    mid = (st + ed) // 2
    length = 0  # 가져가는 나무 길이

    for t in tree:
        if t > mid:
            length += t-mid

    if length >= M:
        st = mid + 1
    else:
        ed = mid - 1

print(ed)