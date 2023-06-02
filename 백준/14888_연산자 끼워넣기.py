# 백준 14888_연산자 끼워넣기

import sys


def dfs(idx, sum_v, p, s, m, d):
    global max_v, min_v

    # 식을 완성한 경우
    if idx == N:
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
        return

    # 덧샘
    if p:
        dfs(idx+1, sum_v + A[idx], p - 1, s, m, d)

    # 뺼셈
    if s:
        dfs(idx + 1, sum_v - A[idx], p, s - 1, m, d)

    # 곱셈
    if m:
        dfs(idx + 1, sum_v * A[idx], p, s, m - 1, d)

    # 나눗셈
    if d:
        dfs(idx + 1, int(sum_v / A[idx]), p, s, m, d - 1)


N = int(sys.stdin.readline().strip())  # 수의 개수
A = list(map(int, sys.stdin.readline().split()))  # 숫자
add, sub, mul, div = map(int, sys.stdin.readline().split())  # 덧셈, 뺼셈, 곱셈, 나눗셈의 개수
max_v = -1e9  # 최댓값
min_v = 1e9  # 최솟값

dfs(1, A[0], add, sub, mul, div)

print(max_v)
print(min_v)
