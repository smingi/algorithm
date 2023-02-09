# 백준 12904_A와 B

import sys


S = list(sys.stdin.readline().strip())  # 시작 문자열
T = list(sys.stdin.readline().strip())  # 목표 문자열
result = 0

while T:
    if T[-1] == "A":
        T.pop()

    elif T[-1] == "B":
        T.pop()
        T.reverse()

    if S == T:
        result = 1
        break

print(result)
