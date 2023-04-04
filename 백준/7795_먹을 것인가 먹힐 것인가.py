# 백준 7795_먹을 것인가 먹힐 것인가

import sys


def search(target):
    s, e = 0, M-1

    while s + 1 < e:
        mid = (s+e) // 2

        if B[mid] < target:
            s = mid

        else:
            e = mid

    if target <= B[s]:
        return 0

    elif target <= B[e]:
        return e

    else:
        return M


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())  # N: A의 크기, M: B의 크기
    A = sorted(list(map(int, sys.stdin.readline().split())))  # A
    B = sorted(list(map(int, sys.stdin.readline().split())))  # B
    result = 0

    for i in range(N):
        result += search(A[i])

    print(result)
