# 백준 10819_차이를 최대로

import sys


def dfs(now, sum_v):
    global max_v

    if sum(visited) == N:
        max_v = max(max_v, sum_v)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(numbers[i], sum_v + abs(now - numbers[i]))
            visited[i] = 0


N = int(sys.stdin.readline().strip())  # 숫자의 개수
numbers = list(map(int, sys.stdin.readline().split()))
visited = [0] * N
max_v = 0

for i in range(N):
    visited[i] = 1
    dfs(numbers[i], 0)
    visited[i] = 0

print(max_v)
