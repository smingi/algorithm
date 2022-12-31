# 백준 1406_에디터

import sys


left_st = list(sys.stdin.readline().strip())  # 초기 문자열
M = int(sys.stdin.readline().strip())  # 명령어의 개수
right_st = []

for _ in range(M):
    command = list(sys.stdin.readline().split())  # 입력받은 명령어

    # 커서를 왼쪽으로 한 칸 이동
    if command[0] == "L":
        if left_st:
            right_st.append(left_st.pop())

    # 커서를 오른쪽으로 한 칸 이동
    elif command[0] == "D":
        if right_st:
            left_st.append(right_st.pop())

    # 커서 왼쪽에 있는 문자를 삭제
    elif command[0] == "B":
        if left_st:
            left_st.pop()

    # 문자를 커서 왼쪽에 추가
    else:
        left_st.append(command[1])

print("".join(left_st) + "".join(reversed(right_st)))
