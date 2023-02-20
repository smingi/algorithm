# 백준 11508_2+1 세일

import sys


n = int(sys.stdin.readline().strip())  # 유제품의 개수
product = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 유제품
product.sort(reverse=True)
result = 0

# 전체 상품
result += sum(product)

# +1 상품
for i in range(1, n+1):
    if i % 3 == 0:
        result -= product[i-1]

print(result)
