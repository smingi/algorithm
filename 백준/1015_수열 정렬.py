# 백준 1015_수열 정렬

import sys


N = int(sys.stdin.readline().strip())  # 수열의 길이
P = list(map(int, sys.stdin.readline().split()))  # 수열
copyP = list(P)
copyP.sort()

for i in range(N):
    index = copyP.index(P[i])
    P[i] = index
    copyP[index] = -1

print(" ".join(map(str, P)))
