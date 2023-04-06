# 백준 11536_줄 세우기

import sys


N = int(sys.stdin.readline().strip())  # 이름의 개수
name = [sys.stdin.readline().strip() for _ in range(N)]

if name == sorted(name):
    print("INCREASING")

elif name == sorted(name, reverse=True):
    print("DECREASING")

else:
    print("NEITHER")
