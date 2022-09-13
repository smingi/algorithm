# 백준 10845_큐

import sys

N = int(input())

q = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        q.append(command[1])

    elif command[0] == "pop":
        if q:
            print(q.pop(0))
        else:
            print(-1)

    elif command[0] == "size":
        print(len(q))

    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    else:
        if q:
            print(q[-1])
        else:
            print(-1)
