# 백준 1748_수 이어 쓰기 1

import sys


N = sys.stdin.readline().strip()  # 1 ~ N
result = 0
cnt = 1

while cnt < len(N):
    result += 9 * (10**(cnt-1)) * cnt
    cnt += 1

result += (int(N) - (10 ** (len(N)-1)) + 1) * len(N)
print(result)
