# 백준 9446_텀 프로젝트

import sys
sys.setrecursionlimit(10**6)


def dfs(now):
    global cnt
    visited[now] = 1
    group.append(now)
    new = select[now]

    if visited[new]:
        if new in group:  # 팀을 구성한 경우
            cnt -= len(group[group.index(new):])

    else:
        dfs(new)


T = int(sys.stdin.readline().strip())  # 테스트케이스
for _ in range(T):
    n = int(sys.stdin.readline().strip())  # 학생의 수
    select = [0] + list(map(int, sys.stdin.readline().split()))  # 선택한 학생 번호
    visited = [0] * (n+1)
    cnt = n  # 팀을 구성하지 못한 사람

    for i in range(1, n+1):
        if not visited[i]:
            group = []  # 연결된 그룹
            dfs(i)

    print(cnt)
