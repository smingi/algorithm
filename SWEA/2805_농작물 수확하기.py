# 2805. 농작물 수확하기

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    field = [list(map(int, input())) for _ in range(n)]
    m = n // 2  # 중간지점
    money = 0  # 수익
    for i in range(len(field)):
        if i <= m:  # 위쪽 삼각형
            for j in range(m - i, m + 1 + i):
                money += field[i][j]
        else:  # 아래쪽 삼각형
            for j in range(i - m, n + m - i):
                money += field[i][j]

    print('#{} {}'.format(tc, money))