# 백준 10828_스택

import sys

N = int(input())

st = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        st.append(command[1])

    elif command[0] == "pop":
        if st:
            print(st.pop())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(st))

    elif command[0] == "empty":
        if st:
            print(0)
        else:
            print(1)

    else:
        if st:
            print(st[-1])
        else:
            print(-1)

