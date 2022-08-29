# 백준 9019_DSLR (pypy3사용)

import sys
from collections import deque


def dslr():
    q = deque()
    q.append([A, ""])
    visited = [False] * 10000
    visited[A] = True

    while q:
        now, command = q.popleft()  # now: 현재 숫자, command: 현재 명령어

        if now == B:  # 목표 숫자와 일치하는지 체크
            print(command)
            break

        # D: 2배로, 9999보다 크면 10000의 나머지
        new_d = (now*2) % 10000
        if new_d == B:
            print(command + "D")
            break
        if not visited[new_d]:
            visited[new_d] = True
            q.append([new_d, command+"D"])

        # S: -1, 0보다 작아지면 9999로 변경
        new_s = now-1
        if new_s < 0:
            new_s = 9999
        if new_s == B:
            print(command + "S")
            break
        if not visited[new_s]:
            visited[new_s] = True
            q.append([new_s, command+"S"])

        # L: 왼쪽으로 이동 1234 -> 2341
        new_l = ((now % 1000) * 10) + (now//1000)
        if new_l == B:
            print(command + "L")
            break
        if not visited[new_l]:
            visited[new_l] = True
            q.append([new_l, command+"L"])

        # R: 오른쪽으로 이동 1234 -> 4123
        new_r = (now // 10) + ((now % 10) * 1000)
        if new_r == B:
            print(command + "R")
            break
        if not visited[new_r]:
            visited[new_r] = True
            q.append([new_r, command+"R"])


T = int(sys.stdin.readline())  # T: 테스트케이스 개수
for _ in range(T):
    A, B = (map(int, sys.stdin.readline().split()))  # A: 시작숫자, B: 변경 후 숫자

    dslr()  # 명령어 탐색
