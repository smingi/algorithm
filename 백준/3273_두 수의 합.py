# 백준 3273_두 수의 합

import sys


n = int(sys.stdin.readline().strip())  # 수열의 크기
A = sorted(list(map(int, sys.stdin.readline().split())))  # 수열
x = int(sys.stdin.readline().strip())  # 목표 숫자
s, e = 0, n-1
result = 0

while s < e:
    now = A[s] + A[e]

    if now == x:
        result += 1
        s += 1
        e -= 1

    elif now < x:
        s += 1

    else:
        e -= 1

print(result)
