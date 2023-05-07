# 백준 1193_분수찾기

import sys


X = int(sys.stdin.readline().strip())  # X 번째
cnt = 1  # 한 줄당 개수

while X > cnt:
    X -= cnt
    cnt += 1  # 줄마다 1개씩 늘어남

if cnt % 2:
    up = cnt - X + 1
    down = X

else:
    up = X
    down = cnt - X + 1

print("{0}/{1}".format(up, down))
