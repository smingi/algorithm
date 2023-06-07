# 백준 14889_스타트와 링크

import sys


def dfs(cnt, idx):
    global min_v

    # 짝을 다 지은경우
    if cnt == N // 2:
        left, right = 0, 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    left += stats[i][j]

                if not visited[i] and not visited[j]:
                    right += stats[i][j]

        min_v = min(min_v, abs(left - right))

    else:
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = 1
                dfs(cnt+1, i+1)
                visited[i] = 0


N = int(sys.stdin.readline().strip())  # 짝수
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 능력치
visited = [0] * N
min_v = 1e9

dfs(0, 0)
print(min_v)
