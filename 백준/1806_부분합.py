# 백준 1806_부분합

import sys


N, S = map(int, sys.stdin.readline().split())  # N: 길이, S: 구해야 하는 합
numbers = list(map(int, sys.stdin.readline().split()))  # 주어진 정수(10000이하)
INF = 100001
min_length = INF  # 최소 길이

st = 0  # 시작 부분
ed = 0  # 끝 부분
now = 0  # 현재 숫자
while True:
    if now >= S:  # S 이상인 경우
        min_length = min(min_length, ed - st)

        # 왼쪽부분 오른쪽으로 한칸 이동
        now -= numbers[st]
        st += 1

    else:
        if ed == N:  # 인덱스 범위 넘을시 종료
            break

        # 오른쪽부분 오른쪽으로 한칸 이동
        now += numbers[ed]
        ed += 1

if min_length == INF:  # 만들수 없는 경우 0을 출력
    min_length = 0

print(min_length)
