# 백준 1946_신입 사원

import sys


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    N = int(sys.stdin.readline().strip())  # 지원자의 수
    rank = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 순위
    rank.sort()
    top_rank = 0
    result = 1

    for i in range(1, N):
        if rank[top_rank][1] > rank[i][1]:
            top_rank = i
            result += 1

    print(result)
