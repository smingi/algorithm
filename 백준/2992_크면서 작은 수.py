# 백준 2992_크면서 작은 수

import sys
from itertools import permutations


X = sys.stdin.readline().strip()  # 주어진 수
permutation = []
for per in sorted(set(permutations(X, len(X)))):
    permutation.append("".join(per))

if X == permutation[-1]:
    print(0)

else:
    print(permutation[permutation.index(X)+1])
