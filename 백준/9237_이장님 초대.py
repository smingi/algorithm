# 백준 9237_이장님 초대

import sys


N = int(sys.stdin.readline().strip())  # 묘목의 수
tree = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)   # 묘목
result = 0

for i in range(1, N+1):
    result = max(result, i + tree[i-1])

print(result+1)
