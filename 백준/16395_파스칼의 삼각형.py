# 백준 16395_파스칼의 삼각형

import sys


n, k = map(int, sys.stdin.readline().split())  # n: 행, k: 열
result = [[] for _ in range(n)]

for i in range(n):  # 행
    for j in range(i+1):  # 열

        # 삼각형에서 1인 부분
        if i == 0 or j == 0 or j == i:
            result[i].append(1)

        # 삼각형에서 1이 아닌 부분
        else:
            result[i].append(result[i-1][j-1] + result[i-1][j])

print(result[n-1][k-1])
