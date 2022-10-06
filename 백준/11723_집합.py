# 백준 11723_집합

import sys

M = int(input())  # 연산수
s = []

for _ in range(M):
    command = sys.stdin.readline().split()

    if command[0] == "add":
        if int(command[1]) not in s:
            s.append(int(command[1]))

    elif command[0] == "remove":
        if int(command[1]) in s:
            s.pop(s.index(int(command[1])))

    elif command[0] == "check":
        if int(command[1]) in s:
            print(1)
        else:
            print(0)

    elif command[0] == "toggle":
        if int(command[1]) in s:
            s.pop(s.index(int(command[1])))
        else:
            s.append(int(command[1]))

    elif command[0] == "all":
        s = [i for i in range(1, 21)]

    elif command[0] == "empty":
        s = []
