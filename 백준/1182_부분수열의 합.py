# 백준 1182_부분수열의 합

import sys


def dfs(idx, sum_v):
    global result

    if idx >= N:
        return

    if sum_v + numbers[idx] == S:
        result += 1

    dfs(idx + 1, sum_v)
    dfs(idx + 1, sum_v + numbers[idx])


N, S = map(int, sys.stdin.readline().split())  # N: 정수의 개수, S: 원소의 합
numbers = list(map(int, sys.stdin.readline().split()))  # 부분수열
result = 0

dfs(0, 0)

print(result)
