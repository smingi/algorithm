# swea 2817 부분 수열의 합


def subset(s, sumv):
    global cnt
    if sumv > K:  # 백트래킹
        return

    if s >= N:  # 종료시점
        if sumv == K:  # 원하는 조건 만족하면 +1
            cnt += 1
        return

    subset(s+1, sumv)
    subset(s+1, sumv+lst[s])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0  # 개수
    subset(0, 0)  # 부분집합
    print('#{} {}'.format(tc, cnt))

