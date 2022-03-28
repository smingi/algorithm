# swea 5215. 햄버거 다이어트


def find_maxv(k, sumv, cal):
    global maxv
    if cal > L:  # 제한
        return

    if k >= N:
        if maxv < sumv:  # 최대값
            maxv = sumv
        return

    find_maxv(k+1, sumv + lst[k][0], cal + lst[k][1])
    find_maxv(k+1, sumv, cal)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())  # N: 재료개수, L: 제한
    lst = [list(map(int, input().split())) for _ in range(N)]  # [맛, 칼로리]
    maxv = 0  # 최대값
    find_maxv(0, 0, 0)  # 재귀
    print('#{} {}'.format(tc, maxv))
