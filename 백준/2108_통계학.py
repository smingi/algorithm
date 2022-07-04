# 백준 2108 통계학

import sys
from collections import Counter

n = int(input())
lst = []

for _ in range(n):
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort()
most_lst = Counter(lst).most_common(2)

print(round(sum(lst)/n))
print(lst[n//2])

if len(most_lst) > 1 and most_lst[0][1] == most_lst[1][1]:
    print(most_lst[1][0])
else:
    print(most_lst[0][0])

print(lst[-1]-lst[0])
