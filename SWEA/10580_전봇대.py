# swea 10580 전봇대


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
