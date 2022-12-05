# 백준 2749_피보나치 수 3

# 풀이 참고 방식
# (Fn+1 Fn) = (1 1) ^ n
# (Fn Fn-1) = (1 0)


def multi(a, b):  # 곱셈 (a*b)
    result = [[0, 0], [0, 0]]  # 곱셈 결과

    for r in range(2):  # 행
        for c in range(2):  # 열
            e = 0  # 요소

            for i in range(2):  # 요소값 구하기
                e += a[r][i] * b[i][c]

            result[r][c] = e % remainder

    return result


def square(a, b):  # 제곱 (a^b)
    if b == 1:
        return a

    divide = square(a, b // 2)  # 분할 정복

    if b % 2:  # 홀수 제곱
        return multi(multi(divide, divide), a)

    else:  # 짝수 제곱
        return multi(divide, divide)


n = int(input())  # n번째 피보나치 수

if n < 3:
    print(1)

else:
    remainder = 1000000  # 나머지를 구해야 하는 수
    matrix = [[1, 1], [1, 0]]  # 행열

    print(square(matrix, n)[0][1])  # [1][0]으로해도 같은 결과
