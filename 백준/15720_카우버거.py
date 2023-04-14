# 백준 15720_카우버거

import sys


B, C, D = map(int, sys.stdin.readline().split())  # B: 버거의 개수, C: 사이드 메뉴의 개수, D: 음료의 개수
bugger = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)  # 버거의 가격
side = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)  # 사이드 메뉴의 가격
drink = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)  # 음료의 가격
total_price = sum(bugger) + sum(side) + sum(drink)
print(total_price)

for i in range(min(B, C, D)):
    total_price -= int((bugger[i] + side[i] + drink[i]) * 0.1)

print(total_price)
