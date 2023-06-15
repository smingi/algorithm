# 백준 2251_물통

import sys
from collections import deque


def bfs():
    def move(a_value, b_value):
        if not visited[a_value][b_value]:
            visited[a_value][b_value] = 1
            q.append([a_value, b_value])

    q = deque()
    visited = [[0] * (B+1) for _ in range(A+1)]
    q.append([0, 0])
    visited[0][0] = 1
    result = []

    while q:
        # a, b의 값
        a, b = q.popleft()

        # c의 값
        c = C - a - b

        # 조건에 맞는 경우
        if a == 0:
            result.append(c)

        # A -> B
        min_v = min(a, B - b)
        move(a - min_v, b + min_v)

        # A -> C
        min_v = min(a,  C - c)
        move(a - min_v, b)

        # B -> A
        min_v = min(b, A - a)
        move(a + min_v, b - min_v)

        # B -> C
        min_v = min(b, C - c)
        move(a, b - min_v)

        # C -> A
        min_v = min(c, A - a)
        move(a + min_v, b)

        # C -> B
        min_v = min(c, B - b)
        move(a, b + min_v)

    return ' '.join(map(str, sorted(result)))


A, B, C = map(int, sys.stdin.readline().split())  # 세 정수
print(bfs())
