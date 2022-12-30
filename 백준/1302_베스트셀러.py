# 백준 1302_베스트셀러

import sys


N = int(sys.stdin.readline().strip())  # 팔린 책의 수
book = [sys.stdin.readline().strip() for _ in range(N)]  # 팔린 책의 이름
book.sort()
max_cnt = 1
tmp_cnt = 1
result = book[0]

for i in range(1, N):
    if max_cnt < tmp_cnt:
        max_cnt = tmp_cnt
        result = book[i-1]

    if book[i-1] == book[i]:
        tmp_cnt += 1

    else:
        tmp_cnt = 1

print(result)
