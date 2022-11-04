# 백준 12851_숨바꼭질 2


from collections import deque


def find():
    q = deque()
    q.append(N)
    visited[N][0] = 1  # 시작 시간을 1초로 시작
    visited[N][1] = 1  # 방법의 수를 1로 시작

    while q:
        now = q.popleft()  # 현재 위치

        for move in [now+1, now-1, now*2]:  # 이동할 수 있는 방법
            if 0 <= move < INF:
                if not visited[move][0]:  # 처음 방문한 경우
                    visited[move][0] = visited[now][0] + 1
                    visited[move][1] = visited[now][1]
                    q.append(move)

                elif visited[move][0] == visited[now][0] + 1:
                    visited[move][1] += visited[now][1]


N, K = map(int, input().split())  # N: 수빈, K: 동생
INF = 100001  # 최대숫자
visited = [[0, 0] for _ in range(INF)]  # 걸린시간, 경우의 수

find()

print(visited[K][0] - 1)  # 최소 시간 출력(처음에 더해준 1을 빼줌)
print(visited[K][1])  # 방법의 수 출력
