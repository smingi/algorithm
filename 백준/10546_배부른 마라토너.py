# 백준 10546_배부른 마라토너

import sys


N = int(sys.stdin.readline().strip())  # 참가자 수
dic = dict()
for _ in range(N):
    name = sys.stdin.readline().strip()  # 참가자 이름

    if name not in dic:
        dic[name] = 1

    else:
        dic[name] += 1

for _ in range(N-1):
    name = sys.stdin.readline().strip()  # 완주자 이름

    dic[name] -= 1

    if dic[name] == 0:
        dic.pop(name)

for key in dic.keys():
    print(key)
