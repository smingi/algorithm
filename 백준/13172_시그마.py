# 백준 13172_시그마

import sys


def calc(n, s):  # 페르마의 소정리
    return s * square(n, remainder-2) % remainder


def square(a, b):  # 제곱 계산
    if b == 1:  # 1제곱인 경우
        return a % remainder

    if b % 2:  # 홀수 제곱인 경우
        return a * square(a, b-1) % remainder

    else:  # 짝수 제곱인 경우
        divide = square(a, b // 2)
        return (divide * divide) % remainder


M = int(input())  # 주사위의 개수
remainder = 1000000007  # 나머지를 구해야할 수
result = 0  # 결과

for _ in range(M):
    N, S = map(int, sys.stdin.readline().split())  # N: 면체, S: 모든 수의 합
    result += calc(N, S)  # 페르마의 소정리를 통해서 계산
    result %= remainder  # 계산한 값의 나머지 구하기

print(result)  # 결과 출력
