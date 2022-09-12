# 백준 10830_행렬 제곱

import sys


def mul(a, b):  # 곱셈 연산
    new_procession = [[0] * N for _ in range(N)]  # 곱셈 결과를 저장한 행렬
    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_procession[i][j] += a[i][k] * b[k][j]

            new_procession[i][j] %= 1000  # 각 원소를 1000으로 나눈 나머지

    return new_procession


def square(a, b):  # 제곱 연산
    if b == 1:  # 1제곱인 경우에도 각 원소를 1000으로 나눈 나머지를 반환하도록 변경
        new_procession = [[0] * N for _ in range(N)]  # 계산 후 저장한 행렬
        for i in range(N):
            for j in range(N):
                new_procession[i][j] = a[i][j] % 1000
        return new_procession

    divide = square(a, b//2)
    if b % 2:  # 홀수 제곱인 경우
        return mul(mul(divide, divide), a)
    else:  # 짝수 제곱인 경우
        return mul(divide, divide)


N, B = map(int, sys.stdin.readline().split())  # N: 행렬 크기, B: 제곱 횟수
procession = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 입력받은 행렬
result = square(procession, B)  # 행렬을 b제곱 한 결과

# 출력
for i in range(N):
    for j in range(N):
        print(result[i][j], end=" ")
    print()
