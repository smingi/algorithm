# 11652_카드

import sys


N = int(sys.stdin.readline().strip())  # 가지고 있는 숫자 카드의 개수
dic = dict()
for _ in range(N):
    card = int(sys.stdin.readline().strip())

    if card in dic:
        dic[card] += 1

    else:
        dic[card] = 1

result = 0
max_cnt = 0
for key in dic.keys():
    if max_cnt < dic[key]:
        result = key
        max_cnt = dic[key]

    elif max_cnt == dic[key] and result > key:
        result = key

print(result)
