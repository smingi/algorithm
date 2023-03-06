# 백준 12871_무한 문자열

import sys


s = sys.stdin.readline().strip()  # 첫번째 문자열
t = sys.stdin.readline().strip()  # 두번째 문자열

ns = s * len(t)
nt = t * len(s)

if ns == nt:
    print(1)

else:
    print(0)
