# 백준 5568_카드 놓기

import sys
from itertools import permutations


n = int(sys.stdin.readline().strip())  # 카드의 개수
k = int(sys.stdin.readline().strip())  # 고르는 카드의 개수
card = [sys.stdin.readline().strip() for _ in range(n)]  # 카드
result = set()

for p in permutations(card, k):
    result.add("".join(p))

print(len(result))
