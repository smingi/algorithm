# 백준 2422_한윤정이 이탈리아에 가서 아이스크림을 사먹는데

import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())  # N: 아이스크림 종류의 수, M: 섞으면 안되는 조합의 수
check = [[0] * (N+1) for _ in range(N+1)]
result = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())  # 섞이면 안되는 맛
    check[a][b] = 1
    check[b][a] = 1

for comb in combinations([i for i in range(1, N+1)], 3):
    if check[comb[0]][comb[1]] or check[comb[0]][comb[2]] or check[comb[1]][comb[2]]:
        continue

    result += 1

print(result)
