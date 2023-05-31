# 백준 3036_링

import sys
import math


N = int(sys.stdin.readline().strip())  # N: 링의 개수
ring = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    gcd = math.gcd(ring[0], ring[i])
    print('{0}/{1}'.format(ring[0]//gcd, ring[i]//gcd))
