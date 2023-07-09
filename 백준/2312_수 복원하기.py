# 백준 2312_수 복원하기

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 양의 정수
    num = 2  # 몫
    cnt = 0  # 개수

    while N >= num:
        if N % num == 0:
            cnt += 1
            N = N // num

        else:
            if cnt > 0:
                print(num, cnt)

            cnt = 0
            num += 1

    if cnt:
        print(num, cnt)
