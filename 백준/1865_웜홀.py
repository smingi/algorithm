# 백준 1865_웜홀

import sys


def bellman(start):  # Bellman-Ford
    distance = [999999999] * (N + 1)
    distance[start] = 0  # 시작지점

    for i in range(1, N+1):
        for s, e, t in path:
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                if i == N:  # 순환이 존재하는지 확인
                    return True
    return False


TC = int(input())  # TC: 테스트케이스
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())  # N: 지점의 수, M: 도로의 개수, W: 웜홀의 개수

    path = []  # 도로 (시작점, 도착지, 걸린시간 - 무방향), 웜홀 (시작점, 도착지, 감소시간 - 방향)

    for _ in range(M):  # 무방향
        S, E, T = map(int, sys.stdin.readline().split())  # S: 시작지점, E: 도착지점, T: 걸린 시간
        path.append([S, E, T])
        path.append([E, S, T])

    for _ in range(W):  # 방향
        S, E, T = map(int, sys.stdin.readline().split())  # S: 시작지점, E: 도착지점, T: 감소 시간
        path.append([S, E, -T])

    if bellman(1):
        print("YES")
    else:
        print("NO")
