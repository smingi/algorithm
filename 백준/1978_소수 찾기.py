# 백준 1978_소수 찾기

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num//2+1):
        if num%i == 0:
            return False

    return True


N = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for number in numbers:
    if is_prime(number):
        cnt += 1

print(cnt)
