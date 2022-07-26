# 백준 1966_프린터 큐


T = int(input())
for _ in range(T):
    N, idx = map(int, input().split())
    q = list(map(int, input().split()))
    order = 0

    while q:
        maxv = max(q)
        doc = q.pop(0)
        order += 1

        if doc != maxv:
            q.append(doc)
            order -= 1

        if doc == maxv and idx == 0:
            print(order)
            break

        if idx == 0:
            idx = len(q)-1
        else:
            idx -= 1
