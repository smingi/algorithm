# 백준 1929_소수 구하기


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False

    return True


M, N = map(int, input().split())
for num in range(M, N+1):
    if is_prime(num):
        print(num)
