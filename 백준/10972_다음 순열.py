# 백준 10972_다음 순열

import sys


def solve():
    global target

    for i in range(N - 1, 0, -1):
        if target[i - 1] < target[i]:
            for j in range(N - 1, 0, -1):
                if target[i - 1] < target[j]:
                    target[i-1], target[j] = target[j], target[i-1]
                    target = target[:i] + sorted(target[i:])
                    return " ".join(map(str, target))

    return -1


N = int(sys.stdin.readline().strip())  # 1 ~ N
target = list(map(int, sys.stdin.readline().split()))  # 순열
print(solve())
