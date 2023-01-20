# 백준 2910_빈도 정렬

import sys


N, C = map(int, sys.stdin.readline().split())  # N개의 수, C 이하
number = list(map(int, sys.stdin.readline().split()))  # 주어진 숫자
idx = 0
lst = []
dic = dict()

for num in number:
    if num not in dic:
        lst.append([idx, num])
        dic[num] = 1
        idx += 1

    else:
        dic[num] += 1

# 빈도가 높은 순, 빈도가 같으면 빨리 나온 순으로 정렬
lst.sort(key=lambda x: [-dic[x[1]], x[0]])

for idx, num in lst:
    for _ in range(dic[num]):
        print(num, end=" ")
