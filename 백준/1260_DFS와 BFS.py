# 백준 1260 DFS와 BFS


def dfs(v):  # dfs 재귀
    print(v, end=' ')
    for i in lst[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)


def bfs(v):  # bfs
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in lst[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    print()


N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    lst[n1].append(n2)
    lst[n2].append(n1)  # 양방향
for i in range(len(lst)):  # 정렬
    lst[i].sort()

visited = [0] * (N + 1)
visited[V] = 1
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
