# 백준 2098_외판원 순회

import sys


def dfs(now, visited):
    if visited == (1 << N) - 1:  # 모든 지역 방문 ex) 8(10000) - 1 = 7(1111)
        if board[now][0] == 0:  # 출발지점으로 가는 경로가 없는 경우
            return INF
        dp[now][visited] = board[now][0]
        return board[now][0]

    if dp[now][visited] != -1:  # 왔던 지점인지 여부
        return dp[now][visited]

    min_v = INF  # 최소 비용
    for i in range(N):
        if not visited & (1 << i) and board[now][i] != 0:
            min_v = min(min_v, board[now][i] + dfs(i, visited | (1 << i)))

    dp[now][visited] = min_v
    return min_v


N = int(input())  # 도시의 수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 비용(0은 갈수 없는 곳)
INF = int(1e9)
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]

print(dfs(0, 1))  # 시작지점, 시작지점 방문 체크 ex) 0000 -> 0001 0번 도시 체크
