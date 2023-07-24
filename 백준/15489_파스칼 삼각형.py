# 백준 15489_파스칼 삼각형

import sys
import math


R, C, W = map(int, sys.stdin.readline().split())  # R: 꼭지점 행, C: 꼭지점 열, W: 길이
result = 0

for i in range(R, R+W):
    for j in range(C, C+i-R+1):
        result += math.comb(i-1, j-1)

print(result)
