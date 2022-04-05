# 백준 2606 바이러스


def bfs(x):
    q = []
    q.append(x)
    while q:
        x = q.pop(0)
        for i in lst[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


N = int(input())
edges = int(input())  # 간선 수
lst = [[] for _ in range(N+1)]

for _ in range(edges):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)  # 양방향

visited = [0] * (N+1)
visited[1] = 1
bfs(1)
print(sum(visited)-1)
