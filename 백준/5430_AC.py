# 백준 5430_AC

import sys
from collections import deque


T = int(input())  # T: 테스트 개수
for _ in range(T):
    p = list(sys.stdin.readline().strip())  # 수행할 함수
    n = int(sys.stdin.readline())  # 배열에 들어있는 개수
    q = deque(sys.stdin.readline()[1:-2].split(","))  # 배열에 들어있는 정수

    if n == 0:  # 비어있는 경우 빈배열로 초기화
        q = deque()

    error = False  # 에러 체크

    index = 0
    for calc in p:
        if calc == "R":  # 뒤집는 연산인 경우 index 를 변경
           index = (index+1) % 2

        else:  # 버리는 연산인 경우
            if q:  # 뺼 값이 있는 경우
                if index == 0:  # 앞에서 뺴는 경우
                    q.popleft()
                else:  # 뒤에서 빼는 경우
                    q.pop()
            else:
                error = True
                break

    if error:  # 에러가 발생했으면 에러 출력
        print("error")

    else:
        if index:  # 역순으로 끝나면 뒤집어줌
            q.reverse()

        print("[{}]".format(','.join(q)))
