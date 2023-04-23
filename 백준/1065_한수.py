# 백준 1065_한수

import sys


N = int(sys.stdin.readline().strip())  # 1000보다 작거나 같은 자연수

if N < 100:
    print(N)

else:
    result = 99

    for i in range(100, N+1):
        num = list(map(int, str(i)))

        if num[0] - num[1] == num[1] - num[2]:
            result += 1

    print(result)
