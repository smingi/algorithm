# 백준 1337_올바른 배열

import sys


N = int(sys.stdin.readline().strip())  # 수의 개수
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
result = 5

for i in range(N):
    cnt = 0

    for j in range(numbers[i]+1, numbers[i]+5):
        if j not in numbers:
            cnt += 1

    result = min(result, cnt)

print(result)
