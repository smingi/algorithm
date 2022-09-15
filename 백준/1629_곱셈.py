# 백준 1629_곱셈


def calc(a, b):
    if b == 1:
        return a % C
    else:
        result = calc(a, b//2)  # 분할 정복 (지수법칙, 나머지 분배법칙)
        if b % 2:
            return (result * result * a) % C
        else:
            return (result * result) % C


A, B, C = map(int, input().split())  # A: 정수  B: 제곱 횟수, C: 나눌 수

print(calc(A, B))
