# 백준 1940_주몽

import sys


N = int(sys.stdin.readline().strip())  # 재료의 개수
M = int(sys.stdin.readline().strip())  # 갑옷을 만드는데 필요한 수
ingredient = list(map(int, sys.stdin.readline().split()))  # 재료
ingredient.sort()

result = 0
s, e = 0, N-1
while s < e:
    if ingredient[s] + ingredient[e] == M:
        result += 1
        s += 1
        e -= 1

    elif ingredient[s] + ingredient[e] < M:
        s += 1

    else:
        e -= 1

print(result)
