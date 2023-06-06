# 백준 10451_순열 사이클

import sys


def find(now):
    global result

    lst = [now]

    while not visited[now]:
        visited[now] = 1
        now = numbers[now]
        lst.append(now)

    if now in lst:
        result += 1


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 순열의 크기
    numbers = [0] + list(map(int, sys.stdin.readline().split()))  # 순열
    visited = [0] * (N + 1)
    result = 0

    for i in range(1, N+1):
        if not visited[i]:
            find(i)

    print(result)
