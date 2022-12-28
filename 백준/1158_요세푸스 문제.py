# 백준 1158_요세푸스 문제

import sys


N, K = map(int, sys.stdin.readline().split())  # N: 사람의 수, K: 양의 정수
q = [i for i in range(1, N+1)]
result = []
index = 0

for i in range(N):
    index = (index+K-1) % len(q)
    num = q.pop(index)
    result.append(num)

print("<", end="")
print(", ".join(map(str, result)), end="")
print(">", end="")
