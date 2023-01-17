# 백준 2002_추월

import sys


N = int(sys.stdin.readline().strip())  # 차의 대수
in_car = dict()  # 차가 들어온 순서[차 이름: 순서]
for i in range(N):
    in_car[sys.stdin.readline().strip()] = i

out_car = [sys.stdin.readline().strip() for _ in range(N)]  # 차가 나온 순서[차 이름]
result = 0

for i in range(N-1):
    for j in range(i+1, N):
        if in_car[out_car[i]] > in_car[out_car[j]]:
            result += 1
            break

print(result)
