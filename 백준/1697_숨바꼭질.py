# 백준 1697_숨바꼭질


from collections import deque


def bfs():
    q = deque()
    q.append(N)

    while q:
        now = q.popleft()  # 현재 위치

        if now == K:  # 목표지점
            print(time[now])
            break

        for location in [now-1, now+1, now*2]:  # 현재 위치에서 갈수 있는 위치
            if 0 <= location <= maxv and not time[location]:  # 범위 내에 가지 않은 곳
                time[location] = time[now]+1  # 걸리는 시간 추가
                q.append(location)  # 다음 위치 추가


N, K = map(int, input().split())
maxv = 100000
time = [0] * (maxv+1)

bfs()
