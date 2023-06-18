# 백준 2847_게임을 만든 동준이

import sys


N = int(sys.stdin.readline().strip())  # 레벨의 수
score = [int(sys.stdin.readline().strip()) for _ in range(N)]  # 점수
result = 0

for i in range(N-1, 0, -1):
    if score[i] <= score[i-1]:
        result += score[i-1] - score[i] + 1
        score[i-1] = score[i] - 1

print(result)
