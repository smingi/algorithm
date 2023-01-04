# 백준 2143_두 배열의 합

import sys
from collections import defaultdict


T = int(sys.stdin.readline().strip())  # 원하는 숫자
n = int(sys.stdin.readline().strip())  # A 배열의 길이
A = list(map(int, sys.stdin.readline().split()))  # 배열 A
m = int(sys.stdin.readline().strip())  # B 배열의 길이
B = list(map(int, sys.stdin.readline().split()))  # 배열 B
sum_dic = defaultdict(int)  # 딕셔너리에 합을 저장

# A 배열의 합 구하기
for i in range(n):
    for j in range(i, n):
        sum_dic[sum(A[i:j+1])] += 1

result = 0  # 결과
# B 배열의 합 구하기
for i in range(m):
    for j in range(i, m):
        result += sum_dic[T - sum(B[i:j+1])]

print(result)
