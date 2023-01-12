# 백준_5397_키로거

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    word = sys.stdin.readline().strip()  # 받은 입력
    left = []  # 왼쪽 부분
    right = []  # 오른쪽 부분

    for w in word:

        # 왼쪽 화살표
        if w == "<":
            if left:
                right.append(left.pop())

        # 오른쪽 화살표
        elif w == ">":
            if right:
                left.append(right.pop())

        # 백스페이스
        elif w == "-":
            if left:
                left.pop()

        # 알파벳 대문자, 소문자, 숫자
        else:
            left.append(w)

    print("".join(left) + "".join(right[::-1]))
