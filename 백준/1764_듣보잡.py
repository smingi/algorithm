# 백준 1764_듣보잡

import sys

N, M = map(int, input().split())  # N: 듣지 못한 사람, M: 보지 못한 사람
n_lst = [sys.stdin.readline().strip() for _ in range(N)]  # 듣지 못한 사람 리스트
m_lst = [sys.stdin.readline().strip() for _ in range(N)]  # 보지 못한 사람 리스트

nm_lst = list(set(n_lst) & set(m_lst))  # 듣지도 보지도 못한 사람
nm_lst.sort()  # 사전순으로 정렬

print(len(nm_lst))  # 듣지도 보지도 못한 사람 수
for name in nm_lst:  # 듣지도 보지도 못한 사람 출력
    print(name)
