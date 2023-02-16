# 백준 1969_DNA

import sys


N, M = map(int, sys.stdin.readline().split())  # N: DNA 의 수, M: 문자열의 길이
DNA = [list(sys.stdin.readline().strip()) for _ in range(N)]  # DNA
dic_num = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
dic_alpha = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
result_DNA = ""
min_distance = 0

for i in range(M):
    cnt = [0] * 4

    for j in range(N):
        cnt[dic_alpha[DNA[j][i]]] += 1

    max_cnt = max(cnt)
    max_index = cnt.index(max_cnt)
    result_DNA += dic_num[max_index]
    min_distance += N - max_cnt

print(result_DNA)
print(min_distance)
