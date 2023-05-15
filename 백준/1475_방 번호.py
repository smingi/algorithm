# 백준 1475_방 번호

import sys
import math


N = sys.stdin.readline().strip()  # 방번호
dic = dict()
result = 0

for num in N:
    if num not in dic:
        dic[num] = 1

    else:
        dic[num] += 1

for i in range(9):
    if i != 6 and str(i) in dic:
        result = max(result, dic[str(i)])

cnt = 0
if '6' in dic:
    cnt += dic['6']

if '9' in dic:
    cnt += dic['9']

print(max(result, math.ceil(cnt/2)))
