# 백준 14241_슬라임 합치기

import sys


N = int(sys.stdin.readline().strip())  # 슬라임의 개수
slime = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)  # 슬라임
result = 0

while len(slime) > 1:
    a = slime.pop(0)
    b = slime.pop(0)
    result += a * b
    slime.append(a+b)

print(result)
