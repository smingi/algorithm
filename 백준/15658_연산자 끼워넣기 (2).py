# 백준 15658_연산자 끼워넣기 (2)

import sys


def dfs(idx, value, a, s, m, d):
    global max_v, min_v

    if idx == N:
        max_v = max(max_v, value)
        min_v = min(min_v, value)

    else:
        if a:
            dfs(idx+1, value + A[idx], a-1, s, m, d)

        if s:
            dfs(idx+1, value - A[idx], a, s-1, m, d)

        if m:
            dfs(idx+1, value * A[idx], a, s, m-1, d)

        if d:
            dfs(idx+1, int(value / A[idx]), a, s, m, d-1)


N = int(sys.stdin.readline().strip())  # 수의 개수
A = list(map(int, sys.stdin.readline().split()))  # 수열
add, sub, mul, div = map(int, sys.stdin.readline().split())  # 연산자의 개수(덧셈, 뺄셈, 곱셈, 나눗셈)
max_v = -1e9
min_v = 1e9

dfs(1, A[0], add, sub, mul, div)

print(max_v)
print(min_v)
