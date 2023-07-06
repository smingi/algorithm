# 백준 12845_모두의 마블

import sys


n = int(sys.stdin.readline().strip())  # 카드의 개수
card = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)  # 카드
result = 0

for i in range(1, n):
    result += card[0] + card[i]

print(result)
