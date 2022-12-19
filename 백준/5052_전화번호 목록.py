# 백준 5052_전화번호 목록

import sys


t = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(t):
    n = int(sys.stdin.readline().strip())  # 전화번호의 수
    numbers = [sys.stdin.readline().strip() for _ in range(n)]  # 전화번호
    numbers.sort()
    result = "YES"

    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            result = "NO"
            break

    print(result)
