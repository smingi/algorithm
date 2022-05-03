# swea 4050 재관이의 대량 할인


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    for i in range(2, N, 3):
        lst[i] = 0

    print('#{} {}'.format(tc, sum(lst)))
