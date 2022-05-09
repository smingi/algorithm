# 10204. 초밥 식사


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    A = 0  # 각 사람별 행복도
    B = 0
    lst.sort(key=lambda x: -(x[0]+x[1]))  # 정렬
    for i in range(N):
        if (i+1) % 2:
            A += lst[i][0]
        else:
            B += lst[i][1]
    print('#{} {}'.format(tc, A - B))
