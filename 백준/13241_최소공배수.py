# 백준 13241_최소공배수

import sys
import math


A, B = map(int, sys.stdin.readline().split())  # 두 정수
print(math.lcm(A, B))
