# 백준 10610_30

import sys


N = list(map(int, sys.stdin.readline().strip()))  # 양수
N.sort(reverse=True)

# 배수 판정법
# 3의 배수 판정 - 모든 자리의 수의 합이 3의 배수이다.
# 10의 배수 판정 - 일의 자리의 수가 0이다.

result = -1
if sum(N) % 3 == 0:
    if N[-1] == 0:
        result = "".join(map(str, N))

print(result)
