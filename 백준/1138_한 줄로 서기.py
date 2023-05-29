# 백준 1138_한 줄로 서기

import sys


N = int(sys.stdin.readline().strip())  # N: 사람의 수
person = list(map(int, sys.stdin.readline().split()))  # 왼쪽에 있는 자신보다 큰 사람의 수
result = [0] * N

for i in range(N):
    cnt = 0

    for j in range(N):
        if cnt == person[i] and result[j] == 0:
            result[j] = i + 1
            break

        elif result[j] == 0:
            cnt += 1

print(*result)
