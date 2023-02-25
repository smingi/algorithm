# 백준 14916_거스름돈

import sys


n = int(sys.stdin.readline().strip())  # 만들어야 하는 수
result = 0

while True:
    if n % 5 == 0:
        result += n//5
        break

    else:
        n -= 2
        result += 1

    if n < 0:
        break

if n < 0:
    print(-1)

else:
    print(result)
