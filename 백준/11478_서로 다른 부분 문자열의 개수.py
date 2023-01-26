# 백준 11478_서로 다른 부분 문자열의 개수

import sys


S = sys.stdin.readline().strip()  # 문자열
result = set()
for cnt in range(1, len(S)+1):
    for i in range(len(S) + 1 - cnt):
        result.add(S[i:i+cnt])

print(len(result))
