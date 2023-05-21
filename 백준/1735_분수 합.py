# 백준 1735_분수 합

import sys
import math


A1, B1 = map(int, sys.stdin.readline().split())  # A1: 분자, B1: 분모
A2, B2 = map(int, sys.stdin.readline().split())  # A2: 분자, B2: 분모

B3 = math.lcm(B1, B2)  # 결과 분모
A3 = (A1 * (B3 // B1)) + (A2 * (B3 // B2))  # 결과 분자
mod = math.gcd(A3, B3)  # 기약분수 형태로 변경

print(A3//mod, B3//mod)
