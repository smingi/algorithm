# 백준 5800_성적 통계

import sys


K = int(sys.stdin.readline().strip())  # 반의 수
for i in range(1, K+1):
    scores = list(map(int, sys.stdin.readline().split()))  # 각 반의 점수
    cnt = scores[0]
    scores = scores[1::]
    scores.sort(reverse=True)
    max_gap = 0

    for j in range(1, cnt):
        max_gap = max(max_gap, scores[j-1] - scores[j])

    print("Class", i)
    print("Max {0}, Min {1}, Largest gap {2}".format(scores[0], scores[-1], max_gap))
