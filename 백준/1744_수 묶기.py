# 백준 1744_수 묶기

import sys
import heapq


N = int(sys.stdin.readline().strip())  # 수열의 길이
plus = []  # 양수
minus = []  # 0 또는 음수
res = []  # 홀수개만 남은 경우

for _ in range(N):
    number = int(sys.stdin.readline().strip())  # 수열의 숫자

    if number > 0:  # 양수인 경우
        heapq.heappush(plus, -number)

    else:  # 0 또는 음수인 경우
        heapq.heappush(minus, number)

result = 0
while plus:  # 양수 계산
    if len(plus) == 1:
        remain = -heapq.heappop(plus)
        res.append(remain)

    else:
        a = -heapq.heappop(plus)
        b = -heapq.heappop(plus)

        if a + b < a * b:
            result += (a * b)

        else:
            result += (a + b)

while minus:  # 음수 계산
    if len(minus) == 1:
        remain = heapq.heappop(minus)
        res.append(remain)

    else:
        a = heapq.heappop(minus)
        b = heapq.heappop(minus)

        if a + b < a * b:
            result += (a * b)

        else:
            result += (a + b)

if res:  # 나머지 계산
    if len(res) > 1:
        if res[0] * res[1] > res[0] + res[1]:
            result += (res[0] * res[1])

        else:
            result += (res[0] + res[1])

    else:
        result += res[0]

print(result)
