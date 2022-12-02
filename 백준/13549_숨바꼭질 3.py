# 백준 13549_숨바꼭질 3


from collections import deque


def find():  # 이동
    q = deque()
    INF = 100001  # 범위 제한
    visited = [0] * INF  # 방문여부, 걸린 시간
    q.append(N)
    visited[N] = 1

    while q:
        now = q.popleft()  # 현재 위치

        if now == K:  # 도착지에 도달하면 종료
            print(visited[now] - 1)  # 처음에 더해준 1을 빼줌
            break

        teleport = now * 2  # 순간이동
        if 0 <= teleport < INF and not visited[teleport]:
            q.appendleft(teleport)
            visited[teleport] = visited[now]

        for move in [now+1, now-1]:  # 이동
            if 0 <= move < INF and not visited[move]:
                q.append(move)
                visited[move] = visited[now] + 1


N, K = map(int, input().split())  # N: 수빈이의 위치, K: 동생의 위치

find()  # 찾기 (너비우선탐색)
