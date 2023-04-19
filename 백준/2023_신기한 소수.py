# 백준 2023_신기한 소수

import sys


# 소수 판별
def check_prime(target):
    for i in range(2, int(target**0.5)+1):
        if target % i == 0:
            return False

    return True


def dfs(target):
    # 조건에 맞는 경우
    if len(str(target)) == N:
        print(target)

    else:
        for num in range(10):
            new_target = target * 10 + num

            if check_prime(new_target):
                dfs(new_target)


N = int(sys.stdin.readline().strip())  # 자릿수
# 1의 자리 소수에서 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)
