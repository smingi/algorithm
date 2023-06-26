# 백준 2485_가로수

import sys
import math


N = int(sys.stdin.readline().strip())  # 가로수의 수
tree = int(sys.stdin.readline().strip())  # 첫번째 나무의 위치
distance = []  # 각 나무 사이의 거리

for i in range(N-1):
    nex_tree = int(sys.stdin.readline().strip())  # 다음 나무의 위치
    distance.append(nex_tree - tree)
    tree = nex_tree

gcd = distance[0]
for i in range(1, N-1):
    gcd = math.gcd(gcd, distance[i])

result = 0
for i in range(N-1):
    result += distance[i] // gcd - 1

print(result)
