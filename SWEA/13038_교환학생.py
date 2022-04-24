# swea 13038 교환학생


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    minv = 987654321

    for i in range(7):  # 완전 탐색
        if lst[i] == 1:
            idx = i
            cnt = 0
            day = 0
            while cnt < N:
                cnt += lst[idx]
                idx = (idx + 1) % 7
                day += 1
            if minv > day:
                minv = day
    print('#{} {}'.format(tc, minv))
